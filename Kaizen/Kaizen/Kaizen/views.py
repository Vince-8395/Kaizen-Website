from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    # return HttpResponse('Welcome to Kaizen Application')
    return render(request, 'Homepage.html')

def LandingPage(request):
    # return HttpResponse('Welcome to Kaizen Application')
    return render(request, 'Landingpage.html')

def About(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')

def Register(request):
    # return HttpResponse('Registration Page')
    return render(request, 'Registration.html')

def article_list(request):
    # return HttpResponse('Article Page')
    return render(request, 'article_list.html')
