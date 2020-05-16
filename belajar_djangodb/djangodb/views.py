from django.shortcuts import render

def index(request):

    context = {
        'judul':'WEBSITE HOME'
    }
    return render(request, 'index.html', context)