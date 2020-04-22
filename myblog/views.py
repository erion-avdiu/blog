from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("Homepage")

def author(request):
    return render(request, 'author.html')