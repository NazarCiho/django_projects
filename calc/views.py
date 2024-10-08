from django.http import HttpResponse, Http404
from django.shortcuts import render

def calculate_multiplication(request, a, b,diya):
    if diya=="*":
        result = a * b
        diya_name = 'МНОЖЕННЯ'
    elif diya=="-":
        result = a - b
        diya_name = 'ВІДНІМАННЯ'
    elif diya=="+":
        result = a + b
        diya_name = 'ДОДАВАННЯ'
    elif diya=="d":
        if b!=0:
            result = int(a / b)
            diya_name = 'Діллення'
        else:
            raise Http404("ДІЛЕННЯ НА НУЛЬ НЕМОЖЛИВЕ")
    else:
        return HttpResponse(f'Ми ще не обробляємо таку дію: "{diya}"')
    response = render(request, 'calc/index.html', {'a': a, 'b': b, 'diya_name': diya_name, 'result': result})
    return response

def calcquery(request):
    try:
        a = int(request.GET.get('a'))
        b = int(request.GET.get('b'))
        result = a * b
        response = render(request, 'calc/index.html', {'a': a, 'b': b, 'diya_name': 'МНОЖЕННЯ', 'result': result})
        return response
    except (TypeError, ValueError):
        return HttpResponse("Ви ввели пенравильні дані 'a' and 'b'")

def index(request):
    return render(request, 'calc/index.html')