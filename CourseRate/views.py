from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    response = render(request, 'CourseRater/home.html', context=context_dict)
    return response

def about(request):
    context_dict = {}
    response = render(request, 'CourseRater/about.html', context=context_dict)
    return response
