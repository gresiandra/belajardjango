from django import forms

class contactForm(forms.Form):

    nama = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class':'form-control'}))

    GENDER = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
    )

    jenis_kelamin = forms.ChoiceField(choices=GENDER, label='Gender')

    TAHUN = range(1960,2021,1)
    tanggal_lahir = forms.DateField(widget=forms.SelectDateWidget(years=TAHUN))
    
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    alamat = forms.CharField(max_length=200, required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    agree = forms.BooleanField()

    def clean_nama(self):
        nama_input = self.cleaned_data.get('nama')

        if nama_input == 'jancok':
            raise forms.ValidationError('Tidak Boleh Kata-Kata Kotor')
