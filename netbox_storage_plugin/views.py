import json
from django.http import JsonResponse
from django.views.generic import View
from netbox.views import generic
from .forms import VolumeForm, DetailsForm
from .models import Volume
from .tables import VolumeTable
from .details_fields import DETAILS_FIELDS


class VolumeListView(generic.ObjectListView):
    queryset = Volume.objects.all()
    table = VolumeTable

class VolumeView(generic.ObjectView):
    queryset = Volume.objects.all()
    template_name = 'netbox_storage_plugin/volume_detail.html'

class VolumeEditView(generic.ObjectEditView):
    queryset = Volume.objects.all()
    form = VolumeForm
    template_name = 'netbox_storage_plugin/volume_edit.html'

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST, instance=self.get_object())
        if form.is_valid():
            volume = form.save(commit=False)
            content_type = form.cleaned_data['content_type']
            object_id = form.cleaned_data['object_id']
            if content_type and object_id:
                # Set the associated_object using content_type and object_id
                volume.associated_object = content_type.get_object_for_this_type(id=object_id)
            else:
                volume.associated_object = None
            volume.save()
            return self.form_valid(form)
        return self.form_invalid(form)

class VolumeDeleteView(generic.ObjectDeleteView):
    queryset = Volume.objects.all()

class VolumeImportView(generic.BulkImportView):
    model = Volume
    template_name = 'netbox_storage_plugin/volume_import.html'

class VolumeBulkEditView(generic.BulkEditView):
    queryset = Volume.objects.all()
    table = VolumeTable

class VolumeBulkDeleteView(generic.BulkDeleteView):
    queryset = Volume.objects.all()
    table = VolumeTable

class VolumeChangeLogView(generic.ObjectChangeLogView):
    base_template = 'netbox_storage_plugin/volume_detail.html'

class GetDetailsFormView(View):
    """
    AJAX view to return the HTML for the details form based on volume type.
    
    This view is called when the volume type is selected or changed, rendering
    the appropriate form fields for the 'details' JSON field.
    
    Methods:
        get: Handle GET requests with 'type' and optional 'details' parameters.
    """
    def get(self, request, *args, **kwargs):
        volume_type = request.GET.get('type')
        details_json = request.GET.get('details', '{}')
        try:
            details = json.loads(details_json)
        except json.JSONDecodeError:
            details = {}
        if volume_type in DETAILS_FIELDS:
            form = DetailsForm(volume_type, initial=details)
            form_html = form.as_p()
        else:
            form_html = ''
        return JsonResponse({'form_html': form_html})