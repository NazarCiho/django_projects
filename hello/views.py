from django.http import HttpResponse
from django.shortcuts import render

def say_hello_path(request, name):
    response = render(request, 'hello/index.html', {'name': name, 'cookies': request.COOKIES})
    response.set_cookie('author', 'Tsikhotskyi')
    return response

def say_hello_query(request):
    name = request.GET.get('name', 'YOU')
    response = render(request, 'hello/index.html', {'name': name, 'cookies': request.COOKIES})
    response.set_cookie('author', 'Tsikhotskyi')
    return response

def index(request):
    return render(request, 'hello/index.html')
