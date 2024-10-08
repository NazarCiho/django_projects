from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def hello(request):
    return render(request, "hello.html")
def landing_page(request):
    return render(request, 'landing_page.html')
