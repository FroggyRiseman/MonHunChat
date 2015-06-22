from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chat/index.html')


def about(request):
    return render(request, 'chat/about.html')
