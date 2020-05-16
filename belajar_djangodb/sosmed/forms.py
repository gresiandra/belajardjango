from django import forms

from .models import sosmedModel

class sosmedForm(forms.ModelForm):
    class Meta:
        model = sosmedModel
        fields = [
            'nama_depan',
            'nama_belakang',
            'username'
        ]

        widgets = {
            'nama_depan': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'nama_belakang': forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),

            'username':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }