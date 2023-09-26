from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Welcome to Kaizen Application')
    return render(request, 'Homepage.html')

def about(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')

def registration(request):
    # return HttpResponse('Registration Page')
    return render(request, 'Registration.html')

def article_list(request):
    # return HttpResponse('Article Page')
    return render(request, 'article_list.html')
