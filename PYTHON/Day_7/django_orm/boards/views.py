from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"boards.html")

def subway(request):
    return render(request,"subway.html")