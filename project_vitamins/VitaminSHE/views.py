from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'VitaminSHE/home.html')

def about(request):
    return HttpResponse('<h1>Webapp About Page</h1>')

