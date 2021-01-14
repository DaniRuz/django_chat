from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Bienvenido a mi blog")