#!/usr/bin/env python3

import requests
import logging
import re
from pynetbox import api
from datetime import datetime
import time

# Configure logging with DEBUG level for detailed output
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG for verbose output
    format='%(asctime)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

# Configuration
PROMETHEUS_URL = "http://4gk-mon-p-dkr01.server.clemson.edu:9090"
NETBOX_URL = "https://o11y.app.clemson.edu/netbox"
NETBOX_API_TOKEN = "25c89f4320476edf29a6cb24a1d2b085b1fd5264"
DEFAULT_DEVICE_ROLE = 1  # Default DeviceRole ID (adjust based on your NetBox setup)

# Headers for Prometheus and NetBox API
prometheus_headers = {"Accept": "application/json"}

# Initialize NetBox client
nb = api(NETBOX_URL, token=NETBOX_API_TOKEN)
logger.debug(f"Initialized NetBox client at {NETBOX_URL} with token {NETBOX_API_TOKEN[:5]}...")

def query_prometheus(query, timeout=10):
    """
    Query Prometheus using direct HTTP requests and return the results as JSON.
    """
    logger.debug(f"Querying Prometheus with query: {query}")
    url = f"{PROMETHEUS_URL}/api/v1/query"
    params = {"query": query}
    try:
        response = requests.get(url, headers=prometheus_headers, params=params, timeout=timeout)
        logger.debug(f"Prometheus response status code: {response.status_code}")
        response.raise_for_status()
        result = response.json()['data']['result']
        logger.debug(f"Prometheus query result for device(s): {result}")
        return result
    except requests.RequestException as e:
        logger.error(f"Failed to query Prometheus: {e}")
        logger.debug(f"Prometheus query details - URL: {url}, Params: {params}, Headers: {prometheus_headers}")
        raise

def get_or_create_device(device_name):
    """
    Get or create a NetBox Device by name using pynetbox, including device name in logs.
    """
    logger.debug(f"Attempting to get or create device: {device_name}")
    try:
        # Try to find by name first
        device = nb.dcim.devices.get(name=device_name)
        if not device:
            logger.debug(f"Device {device_name} not found by name, attempting creation for device {device_name}...")
            # Create device with required fields
            device_data = {
                "name": device_name,
                "device_type": 1,  # Adjust default device type ID
                "site": 1,         # Adjust default site ID
                "status": "active",
                "role": DEFAULT_DEVICE_ROLE,  # Add required role field
            }
            device = nb.dcim.devices.create(device_data)
            logger.info(f"Created new device: {device_name} with ID: {device.id} for device {device_name}")
        else:
            logger.debug(f"Found existing device: {device_name} with ID: {device.id} for device {device_name}")
        return device
    except Exception as e:
        logger.error(f"Failed to handle device {device_name}: {e} for device {device_name}")
        logger.debug(f"Device query details - URL: {nb.dcim.devices.url}, Name: {device_name} for device {device_name}")
        return None

def get_zpool_state():
    """
    Query zpool state from Prometheus for state == 1 and return a mapping of zpools to devices, ensuring device uniqueness, including device name and state in logs.
    """
    logger.debug("Fetching zpool state from Prometheus (state == 1)")
    try:
        query = 'node_zfs_zpool_state == 1'  # Filter for state exactly equal to 1
        zpool_data = query_prometheus(query)
        logger.debug(f"Zpool data retrieved for device(s): {zpool_data}")
        zpools = {}  # Use dictionary with (zpool_name, nodename) as key to ensure device uniqueness
        zpool_states = {}  # Track states for each zpool-device pair

        for zpool in zpool_data:
            metrics = zpool['metric']
            zpool_name = metrics.get('zpool', '')
            nodename = metrics.get('nodename', '')  # Use nodename directly from the metric
            state = metrics.get('state', '')
            if not zpool_name or not nodename or not state:
                logger.warning(f"Skipping zpool entry due to missing zpool, nodename, or state for device(s): {metrics}")
                continue
            logger.debug(f"Processing zpool {zpool_name} with state {state} for device {nodename} for device {nodename}")

            # Use (zpool_name, nodename) as key to ensure uniqueness per device
            key = (zpool_name, nodename)
            if key not in zpools:
                zpools[key] = nodename
                zpool_states[key] = state

        # Finalize zpool mapping with the state, ensuring device uniqueness
        final_zpools = {}
        for (zpool_name, nodename), _ in zpools.items():
            final_zpools[zpool_name] = {
                'nodename': nodename,
                'state': zpool_states[(zpool_name, nodename)]
            }
            logger.debug(f"Final mapping for zpool {zpool_name} to device {nodename} with state {zpool_states[(zpool_name, nodename)]} for device {nodename}")

        logger.debug(f"Final zpool mapping for device(s): {final_zpools}")
        return final_zpools
    except Exception as e:
        logger.error(f"Failed to fetch zpool state: {e} for device(s)")
        logger.debug(f"Zpool state query details - Query: {query} for device(s)")
        return {}

def get_dataset_info():
    """
    Query dataset information per zpool from Prometheus and return a mapping of datasets to zpools and devices, including device name in logs.
    """
    logger.debug("Fetching dataset info from Prometheus")
    try:
        query = 'node_zfs_zpool_dataset_nread'
        dataset_data = query_prometheus(query)
        logger.debug(f"Dataset data retrieved for device(s): {dataset_data}")
        datasets = {}
        for dataset in dataset_data:
            metrics = dataset['metric']
            dataset_name = metrics.get('dataset', '')
            zpool_name = metrics.get('zpool', '')
            nodename = metrics.get('nodename', '')  # Add nodename to associate datasets with devices
            if not dataset_name or not zpool_name or not nodename:
                logger.warning(f"Skipping dataset entry due to missing dataset, zpool, or nodename for device(s): {metrics}")
                continue
            logger.debug(f"Mapping dataset {dataset_name} to zpool {zpool_name} for device {nodename} for device {nodename}")
            datasets.setdefault((zpool_name, nodename), []).append(dataset_name)  # Use tuple of (zpool_name, nodename) as key
        logger.debug(f"Final dataset mapping for device(s): {datasets}")
        return datasets
    except Exception as e:
        logger.error(f"Failed to fetch dataset info: {e} for device(s)")
        logger.debug(f"Dataset info query details - Query: {query} for device(s)")
        return {}

def import_zfs_storage():
    """
    Collect zpool (LogicalDrive), dataset (Filesystem), and share (Share) information from Prometheus and import into NetBox
    using pynetbox, associating with devices via nodename, including device name in logs, ensuring unique identification by name, zpool, and device.
    """
    logger.debug("Starting ZFS storage import process for device(s)")
    # Query zpool and dataset information from Prometheus
    zpools = get_zpool_state()
    datasets = get_dataset_info()

    if not datasets:  # Check datasets instead of zpools for inclusivity
        logger.info("No dataset information found in Prometheus for device(s).")
        return

    created_logicaldrives = 0
    created_filesystems = 0
    created_shares = 0
    updated_count = 0
    processed_devices = {}  # Track processed devices to avoid duplicates

    # Static mapping of ContentType IDs (as provided)
    DEVICE_CONTENT_TYPE_ID = 42  # dcim.device
    LOGICALDRIVE_CONTENT_TYPE_ID = 199  # storage.logicaldrive
    FILESYSTEM_CONTENT_TYPE_ID = 200  # storage.filesystem
    SHARE_CONTENT_TYPE_ID = 201  # storage.share (assuming this exists)

    # Loop over datasets to ensure all devices and zpools are processed
    for (zpool_name, nodename), dataset_names in datasets.items():
        logger.debug(f"Processing zpool {zpool_name} and datasets for device {nodename}")
        # Get or create the device based on nodename
        if nodename not in processed_devices:
            device = get_or_create_device(nodename)
            if not device:
                logger.error(f"Cannot proceed with zpool {zpool_name} due to missing device {nodename} for device {nodename}")
                continue
            processed_devices[nodename] = device
            logger.debug(f"Device {nodename} processed with ID: {device.id} for device {nodename}")

        # Ensure zpool exists and get its state from zpools (if available)
        zpool_info = zpools.get(zpool_name, {'nodename': nodename, 'state': 'unknown'})
        zpool_state = zpool_info['state']
        logger.debug(f"Processing zpool {zpool_name} for device {nodename} with state {zpool_state}")

        # Create or update LogicalDrive (zpool) in NetBox plugin, ensuring uniqueness by name and device
        try:
            # Look up LogicalDrive by name and associated device (via associated_object_type and associated_object_id)
            logicaldrive_query = {
                "name": zpool_name,
                "associated_object_id": device.id,
            }
            logger.debug(f"Querying LogicalDrives with: {logicaldrive_query}")
            logicaldrives = nb.plugins.storage.logicaldrives.filter(**logicaldrive_query)
            logger.debug(f"LogicalDrives result count: {len(logicaldrives)}")
            logicaldrive = list(logicaldrives)[0] if logicaldrives else None  # Wrap in list() before indexing [0]

            if logicaldrive:
                logger.debug(f"Found LogicalDrive: {logicaldrive.name} (ID: {logicaldrive.id}) for device {nodename}")
            else:
                logger.debug(f"No existing LogicalDrive found for {zpool_name} on device {nodename}")

            logicaldrive_data = {
                "name": zpool_name,
                "description": f"ZFS zpool {zpool_name} on device {nodename} (state: {zpool_state})",
                "type": "zpool",
                "identifier": zpool_name,
                "associated_object_type": DEVICE_CONTENT_TYPE_ID,  # Use static ContentType ID for Device
                "associated_object_id": device.id,  # Link to Device
                "state": zpool_state,  # Assuming 'state' is the correct field name for LogicalDrive
            }
            if logicaldrive:
                logger.debug(f"Updating existing LogicalDrive: {zpool_name} (ID: {logicaldrive.id}) for device {nodename}")
                logicaldrive.update(logicaldrive_data)
                logger.info(f"Updated existing LogicalDrive: {zpool_name} for device {nodename}")
                updated_count += 1
            else:
                logger.debug(f"Creating new LogicalDrive: {zpool_name} for device {nodename}")
                logicaldrive = nb.plugins.storage.logicaldrives.create(logicaldrive_data)
                logger.info(f"Created new LogicalDrive: {zpool_name} with ID: {logicaldrive.id} for device {nodename}")
                created_logicaldrives += 1

            # Create or update Filesystems (datasets) and Shares for this zpool, ensuring uniqueness by name, zpool, and device
            logger.debug(f"Processing datasets for zpool {zpool_name} on device {nodename}: {dataset_names}")
            for dataset_name in dataset_names:
                # Look up Filesystem by name, zpool (via LogicalDrive), and associated device (via associated_object_type and associated_object_id)
                filesystem_query = {
                    "name": dataset_name,
                    "associated_object_id": device.id,
                }
                logger.debug(f"Querying Filesystems with: {filesystem_query}")
                filesystems = nb.plugins.storage.filesystems.filter(**filesystem_query)
                logger.debug(f"Filesystems result count: {len(filesystems)}")
                filesystem = list(filesystems)[0] if filesystems else None  # Wrap in list() before indexing [0]

                if filesystem:
                    logger.debug(f"Found Filesystem: {filesystem.name} (ID: {filesystem.id}) for device {nodename}")
                else:
                    logger.debug(f"No existing Filesystem found for {dataset_name} on device {nodename}")

                filesystem_data = {
                    "name": dataset_name,
                    "description": f"ZFS dataset {dataset_name} in LogicalDrive {zpool_name}",
                    "fs_type": "zfs",  # Example, adjust based on your model
                    "mount_point": f"/{dataset_name}",
                    "associated_object_type": DEVICE_CONTENT_TYPE_ID,  # Use static ContentType ID for Device
                    "associated_object_id": device.id,  # Link to Device
                    "parent_object_type": LOGICALDRIVE_CONTENT_TYPE_ID,  # Use static ContentType ID for LogicalDrive
                    "parent_object_id": logicaldrive.id,  # Link to LogicalDrive as parent
                    "state": "online"
                }
                if filesystem:
                    logger.debug(f"Updating existing Filesystem: {dataset_name} (ID: {filesystem.id}) for device {nodename}")
                    filesystem.update(filesystem_data)
                    logger.info(f"Updated existing Filesystem: {dataset_name} for device {nodename}")
                    updated_count += 1
                else:
                    logger.debug(f"Creating new Filesystem: {dataset_name} for device {nodename}")
                    filesystem = nb.plugins.storage.filesystems.create(filesystem_data)
                    logger.info(f"Created new Filesystem: {dataset_name} with ID: {filesystem.id} for device {nodename}")
                    created_filesystems += 1

                # Check if the filesystem name matches the pattern 'XXX/cifs/YYY' using regex and create/update a Share object
                pattern = r'^.*/(cifs|nfs)/(.+)$'  # Matches any string ending with '/cifs/' followed by any characters (capturing YYY)
                match = re.match(pattern, dataset_name)
                if match:
                    share_name = match.group(2)  # Use the captured YYY as the share name
                    protocol = match.group(1)

                    logger.debug(f"Detected share pattern in Filesystem {dataset_name}, creating/updating Share {share_name} for device {nodename}")

                    # Look up Share by name and associated device (via associated_object_type and associated_object_id)
                    share_query = {
                        "name": share_name,
                        "associated_object_id": device.id,
                    }
                    logger.debug(f"Querying Shares with: {share_query}")
                    shares = nb.plugins.storage.shares.filter(**share_query)
                    logger.debug(f"Shares result count: {len(shares)}")
                    share = list(shares)[0] if shares else None  # Wrap in list() before indexing [0]

                    if share:
                        logger.debug(f"Found Share: {share.name} (ID: {share.id}) for device {nodename}")
                    else:
                        logger.debug(f"No existing Share found for {share_name} on device {nodename}")

                    share_data = {
                        "name": share_name,
                        "description": f"{protocol} share for Filesystem {dataset_name} on device {nodename}",
                        "protocol": protocol,
                        "export_path": share_name,
                        "associated_object_type": DEVICE_CONTENT_TYPE_ID,
                        "associated_object_id": device.id,
                        "parent_object_type": FILESYSTEM_CONTENT_TYPE_ID,
                        "parent_object_id": filesystem.id,
                        "state": "online"
                    }
                    if share:
                        logger.debug(f"Updating existing Share: {share_name} (ID: {share.id}) for device {nodename}")
                        share.update(share_data)
                        logger.info(f"Updated existing Share: {share_name} for device {nodename}")
                        updated_count += 1
                    else:
                        logger.debug(f"Creating new Share: {share_name} for device {nodename}")
                        share = nb.plugins.storage.shares.create(share_data)
                        logger.info(f"Created new Share: {share_name} with ID: {share.id} for device {nodename}")
                        created_shares += 1

        except Exception as e:
            logger.error(f"Failed to process zpool {zpool_name} or its datasets/shares: {e} for device {nodename}")
            logger.debug(f"Error details - Zpool: {zpool_name}, Nodename: {nodename}, Exception: {str(e)} for device {nodename}")

    logger.info(f"Import complete. Created LogicalDrives: {created_logicaldrives}, Filesystems: {created_filesystems}, Shares: {created_shares}, Updated: {updated_count} for device(s)")
    logger.debug("Script execution completed successfully for device(s)")

if __name__ == "__main__":
    try:
        logger.debug("Script execution started for device(s)")
        import_zfs_storage()
    except Exception as e:
        logger.error(f"Script failed: {e} for device(s)")
        logger.debug(f"Script failure details: {str(e)} for device(s)")