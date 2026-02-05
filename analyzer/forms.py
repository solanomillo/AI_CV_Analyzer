from django import forms
from .models import Analysis


class CVUploadForm(forms.ModelForm):
    """
    Formulario para cargar CV y seleccionar puesto objetivo
    """

    class Meta:
        model = Analysis
        fields = ['cv_file', 'target_position']
        widgets = {
            'target_position': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
        }

    cv_file = forms.FileField(
        label="Subí tu CV en PDF",
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'accept': 'application/pdf'
            }
        )
    )
