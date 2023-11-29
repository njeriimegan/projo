from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def error(request):
    return render(request, '404.html')

def blog(request):
    return render(request, 'blog.html')

def book(request):
    return render(request, 'book.html')

def event(request):
    return render(request, 'event.html')

def menu (request):
    return render(request, 'menu.html')


