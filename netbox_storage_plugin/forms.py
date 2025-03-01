from django import forms
from netbox.forms import NetBoxModelForm
from .models import Volume
from .details_fields import DETAILS_FIELDS

class VolumeForm(NetBoxModelForm):
    details = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Volume
        fields = '__all__'

class DetailsForm(forms.Form):
    def __init__(self, volume_type, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_def in DETAILS_FIELDS.get(volume_type, []):
            field_name = field_def['form_field']
            widget = field_def['widget']
            label = field_def['label']
            help_text = field_def['help_text']
            if 'choices' in field_def:
                widget = forms.ChoiceField(choices=field_def['choices'])
            self.fields[field_name] = widget(label=label, help_text=help_text, required=True)