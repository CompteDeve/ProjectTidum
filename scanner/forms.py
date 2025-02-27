from django import forms
from .models import ScanResult

class ScanResultForm(forms.ModelForm):
    class Meta:
        model = ScanResult
        fields = ['domain', 'ip', 'ports']
