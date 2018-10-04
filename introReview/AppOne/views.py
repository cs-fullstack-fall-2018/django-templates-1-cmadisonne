from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newroute (request):
    firstview= '<em>My First App</em>'
    return HttpResponse(firstview)
