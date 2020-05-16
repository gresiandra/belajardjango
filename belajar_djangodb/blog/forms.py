from django import forms

from .models import Post

class blogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
            'category',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Isi dengan judul'
                }
            ),

            'body': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Isi dengan content blog'
                }
            ),

            'email':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Isi dengan alamat email valid'
                }
            ),

            'category':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Isi dengan kategori'
                }
            )
        }
