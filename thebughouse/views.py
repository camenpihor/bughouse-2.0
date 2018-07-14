from django.http import Http404
from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def archive(request):
    return render(request, 'base.html', {'page_name': 'Archive'})


def authors(request):
    return render(request, 'base.html', {'page_name': 'Authors'})


def post(request):
    return render(request, 'base.html', {'page_name': 'Post'})


def control(request):
    return render(request, 'base.html', {'page_name': 'Control'})


def discussion(request):
    return render(request, 'base.html', {'page_name': 'Discussion'})


def user(request, form_type):
    if form_type in ('sign-in', 'sign-up', 'forgot-password'):
        return render(request, 'user.html', {'page_name': 'User', 'form_type': form_type})
    raise Http404
