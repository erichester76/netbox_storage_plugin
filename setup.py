from setuptools import setup, find_packages

setup(
    name="netbox-storage-plugin",
    version="0.2.0",  # Update this as needed
    author="Eric Hester",
    author_email="hester1@clemson.edu",
    description="Netbox Plugin for Storage Volumes",
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),  # Automatically discover Python packages
    include_package_data=True,  # Include additional files from MANIFEST.in
)