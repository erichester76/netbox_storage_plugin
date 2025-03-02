from django import forms
from django.core.exceptions import ValidationError
from .models import Volume
from .details_fields import DETAILS_FIELDS, RELATIONSHIP_RULES

class VolumeForm(forms.ModelForm):
    """
    A form for creating and editing Volume instances, with dynamic type-specific fields
    and validation based on RELATIONSHIP_RULES.
    """

    # Dynamically add type-specific fields from DETAILS_FIELDS
    for volume_type, fields in DETAILS_FIELDS.items():
        for field_def in fields:
            field_name = field_def['form_field']
            field_class = field_def['field_class']
            kwargs = field_def['kwargs']
            # Initialize the field using only kwargs
            locals()[field_name] = field_class(**kwargs)

    class Meta:
        model = Volume
        fields = ['name', 'type', 'parent', 'size', 'details', 'description']
        labels = {
            'name': 'Name',
            'type': 'Type',
            'parent': 'Parent',
            'associated_object': 'Associated Object',
            'size': 'Size',
            'details': 'Details',
            'description': 'Description',
        }
        help_texts = {
            'name': 'A human-readable name for the volume (e.g., "Disk 1", "Data Share")',
            'type': 'The type of storage entity',
            'parent': 'The parent volume, if this volume is part of a hierarchy (e.g., a filesystem on a logical drive)',
            'size': 'The size of the volume in bytes (e.g., 1,073,741,824 for 1 GB)',
        }

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
                    self.fields[field_name].initial = details.get(field_def['json_key'])

    def clean(self):
        """Validate the form and map type-specific fields to the details JSON field."""
        cleaned_data = super().clean()
        volume_type = cleaned_data.get('type')
        parent = cleaned_data.get('parent')
        associated_object = cleaned_data.get('associated_object')

        # Validate parent and associated_object using RELATIONSHIP_RULES
        if volume_type in RELATIONSHIP_RULES:
            rules = RELATIONSHIP_RULES[volume_type]

            # Validate parent
            if parent:
                if parent.type not in rules['allowed_parents']:
                    raise ValidationError({
                        'parent': f"Invalid parent type. Allowed types: {', '.join(rules['allowed_parents'])}"
                    })

            # Validate associated_object
            if associated_object:
                model_name = associated_object._meta.model.__name__
                if model_name not in rules['allowed_associations']:
                    raise ValidationError({
                        'associated_object': f"Invalid associated object. Allowed models: {', '.join(rules['allowed_associations'])}"
                    })

        # Map type-specific fields to the details JSON field
        if volume_type in DETAILS_FIELDS:
            details = {}
            for field_def in DETAILS_FIELDS[volume_type]:
                field_name = field_def['form_field']
                value = cleaned_data.get(field_name)
                if value is not None:
                    details[field_def['json_key']] = value
                # Enforce required fields as defined in kwargs
                if field_def['kwargs'].get('required', False) and value in (None, ''):
                    self.add_error(field_name, f"{field_def['kwargs']['label']} is required for {volume_type} type.")
            cleaned_data['details'] = details

        return cleaned_data