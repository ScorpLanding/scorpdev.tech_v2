from django.shortcuts import render

def projects(request):
    return render(request, 'projects/projects.html')

def instloader(request):
    return  render(request, 'projects/instaloader.html')