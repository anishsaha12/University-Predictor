from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'mirage/index.html', {})

def colprob(request):
    return render(request, 'mirage/courses.html', {})

def predcol(request):
    return render(request, 'mirage/elements.html', {})

def convertgpa(request):
    return render(request, 'mirage/course-details.html', {})

def contact(request):
    return render(request, 'mirage/contacts.html', {})