from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def index(request):
    return HttpResponse("Hello world")
def index1(request):
    return HttpResponse("karpagam")
def index2(request):
    template=loader.get_template('myapp.html')
    return HttpResponse(template.render())