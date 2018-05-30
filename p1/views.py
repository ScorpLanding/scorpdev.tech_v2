from django.shortcuts import render

def index(request):
    return render(request, 'p1/team.html')
