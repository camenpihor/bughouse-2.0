from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def archive(request):
    return render(request, 'base.html')


def authors(request):
    return render(request, 'base.html')


def post(request):
    return render(request, 'base.html')


def control(request):
    return render(request, 'base.html')


def discussion(request):
    return render(request, 'base.html')
