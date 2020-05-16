from django.shortcuts import render, redirect

from . import models
from . import forms

def index(request):

    post_form = forms.blogForm(request.POST or None)

    posts = models.Post.objects.all()
    print(posts)

    context = {
        'Judul':'WEBSITE BLOG',
        'Posts': posts,
        'post_form':post_form
    }

    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()

    return render(request, 'blog/index.html', context)

def ragamPost(request, Input):

    post_form = forms.blogForm(request.POST or None)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()

    posts = models.Post.objects.filter(category=Input)
    context = {
        'Judul':'WEBSITE BLOG '+ Input,
        'Posts': posts,
        'post_form':post_form,
    }

    return render(request, 'blog/index.html', context)