from django import forms
from django.core.exceptions import ValidationError
from .models import Volume
from .details_fields import DETAILS_FIELDS, RELATIONSHIP_RULES

class VolumeForm(forms.ModelForm):
    # Dynamically add type-specific fields from DETAILS_FIELDS
    for volume_type, fields in DETAILS_FIELDS.items():
        for field_def in fields:
            field_name = field_def['form_field']
            field_class = field_def['field_class']
            kwargs = field_def['kwargs']
            # Create the field with the specified class and kwargs
            locals()[field_name] = field_class(**kwargs)

    class Meta:
        model = Volume
        fields = ['name', 'type', 'parent', 'size', 'details', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Example: Dynamically add fields based on DETAILS_FIELDS
        for volume_type, fields in DETAILS_FIELDS.items():
            for field_def in fields:
                field_name = field_def['form_field']
                # Add field if not already present; adjust field type as needed
                if field_name not in self.fields:
                    self.fields[field_name] = forms.CharField(
                        label=field_def.get('label', field_name),
                        required=False,
                        help_text=field_def.get('help_text', '')
                    )

    def clean(self):
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
                # You could add checks for max_depth or multiple_parents here if needed

            # Validate associated_object
            if associated_object:
                model_name = associated_object._meta.model.__name__
                if model_name not in rules['allowed_associations']:
                    raise ValidationError({
                        'associated_object': f"Invalid associated object. Allowed models: {', '.join(rules['allowed_associations'])}"
                    })
                # You could add checks for multiple_associations here if needed

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