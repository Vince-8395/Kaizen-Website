from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Welcome to Kaizen Application')
    return render(request, 'Homepage.html')

def about(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')