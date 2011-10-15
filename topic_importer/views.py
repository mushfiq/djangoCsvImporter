from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.conf import settings

def index(request):
    print request
    return HttpResponse("<h1>Hi</h1>");
