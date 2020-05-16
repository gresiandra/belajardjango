from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import forms
from . import models


def index(request):

    data_diri = models.contactModel.objects.all()
    contact_form = forms.contactForm(request.POST or None)

    context = {
        'heading':'Contact Form',
        'contact_form':contact_form,
        'data_diri':data_diri
    }

    if request.method == 'POST':
        
        if contact_form.is_valid():

            models.contactModel.objects.create(
                nama = contact_form.cleaned_data.get('nama'),
                jenis_kelamin = contact_form.cleaned_data.get('jenis_kelamin'),
                email = contact_form.cleaned_data.get('email'),
                alamat = contact_form.cleaned_data.get('alamat'),
            )
    print(request.POST)
    return render(request, 'contact/index.html', context)