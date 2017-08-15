from django.shortcuts import render
from django.http import HttpResponse


def world(request):
    return render(request, 'personal/home.html')
