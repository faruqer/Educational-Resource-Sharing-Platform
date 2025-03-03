from django import forms

from .models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('title', 'description', 'category', 'resource_type', 'file', 'external_url')

    def clean(self):
        cleaned_data = super().clean()
        file_data = cleaned_data.get('file')
        external_url = cleaned_data.get('external_url')
        if not file_data and not external_url:
            raise forms.ValidationError('Provide either a file or an external URL.')
        return cleaned_data
