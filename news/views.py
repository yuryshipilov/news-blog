from django.shortcuts import render

def index(request):
    return render(request, 'news/index.html')

def about(request):
    return render(request, 'news/about.html')
