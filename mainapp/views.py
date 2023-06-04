from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'pages/home.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def projects(request):
    context = {}
    return render(request, 'pages/projects.html', context)

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)