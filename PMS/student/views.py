from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def studnet_home(request):
    return HttpResponse('Home harsh sexy kam')
