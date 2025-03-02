from django import forms
from netbox.forms import NetBoxModelForm
from django.contrib.contenttypes.models import ContentType
from .models import Volume
from django.core.exceptions import ValidationError
from .details_fields import RELATIONSHIP_RULES, DETAILS_FIELDS

class VolumeForm(forms.ModelForm):
    # Define type-specific fields dynamically from DETAILS_FIELDS
    for volume_type, fields in DETAILS_FIELDS.items():
        for field_def in fields:
            field_name = field_def['form_field']
            widget = field_def['widget']
            label = field_def['label']
            help_text = field_def['help_text']
            kwargs = {'label': label, 'help_text': help_text, 'required': False}
            if 'choices' in field_def:
                kwargs['choices'] = field_def['choices']
            locals()[field_name] = widget(**kwargs)

    class Meta:
        model = Volume
        fields = ['name', 'type', 'parent', 'associated_object', 'size', 'details', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hide the details JSON field from the user
        self.fields['details'].widget = forms.HiddenInput()
        # If editing an existing volume, populate type-specific fields from details
        if self.instance and self.instance.pk:
            details = self.instance.details or {}
            volume_type = self.instance.type
            for field_def in DETAILS_FIELDS.get(volume_type, []):
                field_name = field_def['form_field']
                if field_name in self.fields:
                    self.fields[field_name].initial = details.get(field_name)

    def clean(self):
        cleaned_data = super().clean()
        volume_type = cleaned_data.get('type')
        details = {}
        # Map type-specific fields to the details JSON field
        if volume_type:
            for field_def in DETAILS_FIELDS.get(volume_type, []):
                field_name = field_def['form_field']
                value = cleaned_data.get(field_name)
                if value is not None:  # Only include non-None values
                    details[field_name] = value
                # Enforce required fields if necessary
                if field_def.get('required', False) and not value:
                    self.add_error(field_name, f"{field_def['label']} is required for {volume_type} type.")
            cleaned_data['details'] = details
        return cleaned_data

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