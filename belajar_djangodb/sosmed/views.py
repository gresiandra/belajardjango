from django.shortcuts import render, redirect

# Create your views here.

from .models import sosmedModel
from .forms import sosmedForm

def index(request):

    semua_akun = sosmedModel.objects.all()

    context = {
        'heading':'Selamat datang di app sosmed',
        'semua_akun': semua_akun
    }

    return render(request, 'sosmed/index.html', context)

def create(request):

    form_sosmed = sosmedForm(request.POST or None)

    if request.method == 'POST':
        if form_sosmed.is_valid():
            form_sosmed.save()
        
        return redirect('sosmed:index')

    context = {
        'heading':'Create User Sosmed',
        'form_sosmed':form_sosmed
    }

    return render(request, 'sosmed/create.html', context)

def delete(request, delete_id):
    sosmedModel.objects.filter(id=delete_id).delete()
    return redirect('sosmed:index')