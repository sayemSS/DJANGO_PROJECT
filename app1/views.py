from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    Students = [
    {
        "id": 101,
        "name": "Sadiqul Islam",
        "age": 12
    }, 
    {
        "id": 102,
        "name": "Julfiker Islam",
        "age": 13
    }, 
    {
        "id": 103,
        "name": "Nazmul Hossian",
        "age": 14
    }
    ]
    return render(request, 'index.html', {'students': Students})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')