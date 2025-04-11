from django import forms
from .models import ExcelDocument

class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelDocument
        fields = ['title', 'description', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }