from django.shortcuts import render

def home(request):
    return render(request, "frontend/home.html")

def map(request):
    return render(request, "frontend/map.html")

def create(request):
    return render(request, "frontend/create.html")

def info(request):
    return render(request, "frontend/info.html")
