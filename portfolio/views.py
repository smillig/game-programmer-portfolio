from django.shortcuts import render

def home(request):
    return render(request, "portfolio/home.html")

def contact(request):
    return render(request, "portfolio/contact.html")

def projects(request):
    return render(request, "portfolio/projects.html")

def resume(request):
    return render(request, "portfolio/resume.html")
