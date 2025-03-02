from django import forms
from netbox.forms import NetBoxModelForm
from .models import Volume
from django.core.exceptions import ValidationError
from details_fields import RELATIONSHIP_RULES, DETAILS_FIELDS

class VolumeForm(NetBoxModelForm):
    class Meta:
        model = Volume
        fields = ['type', 'parent', 'associated_object', 'name']  # Example fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Dynamically filter parent choices based on type (if type is set)
        if 'type' in self.data or self.instance.type:
            volume_type = self.data.get('type', self.instance.type)
            if volume_type in RELATIONSHIP_RULES_V2:
                allowed_parents = RELATIONSHIP_RULES_V2[volume_type]['allowed_parents']
                self.fields['parent'].queryset = Volume.objects.filter(type__in=allowed_parents)

    def clean(self):
        cleaned_data = super().clean()
        volume_type = cleaned_data.get('type')
        parent = cleaned_data.get('parent')
        associated_object = cleaned_data.get('associated_object')

        if volume_type not in RELATIONSHIP_RULES_V2:
            return cleaned_data  # No rules defined, skip validation

        rules = RELATIONSHIP_RULES_V2[volume_type]

        # Validate parent
        if parent:
            if parent.type not in rules['allowed_parents']:
                raise ValidationError({
                    'parent': f"Invalid parent type. Allowed types: {', '.join(rules['allowed_parents'])}"
                })
            if not rules['multiple_parents'] and Volume.objects.filter(parent=parent).exists():
                raise ValidationError({
                    'parent': "This parent already has a child, and multiple parents are not allowed."
                })
            # Check hierarchy depth
            depth = self._calculate_depth(parent) + 1
            if depth > rules['max_depth']:
                raise ValidationError({
                    'parent': f"Maximum hierarchy depth ({rules['max_depth']}) exceeded."
                })

        # Validate associated object
        if associated_object:
            model_name = associated_object._meta.model.__name__
            if model_name not in rules['allowed_associations']:
                raise ValidationError({
                    'associated_object': f"Invalid associated object. Allowed models: {', '.join(rules['allowed_associations'])}"
                })
            if not rules['multiple_associations'] and Volume.objects.filter(
                associated_object=associated_object
            ).exists():
                raise ValidationError({
                    'associated_object': "This object is already associated with another volume."
                })

        return cleaned_data

    def _calculate_depth(self, volume, current_depth=0):
        """Recursively calculate the depth of the hierarchy."""
        if not volume or not volume.parent:
            return current_depth
        return self._calculate_depth(volume.parent, current_depth + 1)

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