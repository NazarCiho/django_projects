from email._header_value_parser import get_token

from django.shortcuts import render,redirect,HttpResponse
import html
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import random
from django.middleware.csrf import get_token



def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    guess = request.GET.get('guess', None)
    message = ''
    if guess is not None:
        guess = int(guess)
        request.session['attempts'] += 1

        if guess < request.session['number']:
            message = 'Спробуйте більше число!'
        elif guess > request.session['number']:
            message = 'Спробуйте менше число!'
        else:
            message = f'Вітаємо! Ви вгадали число {request.session["number"]} за {request.session["attempts"]} спроб!'
            del request.session['number']  # Скидаємо гру
    return render(request, 'guess_game/index.html', {'message': message})

def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

def getform(request):
    response = """
        <p>Impossible GET guessing game...</p>
        <form>
        <p>
          <label for="guess">Input Guess</label>
          <input type="text" name="guess" size="40" id="guess"/>
          <input type="hidden" name="csrfmiddlewaretoken" 
            value="token"/>
        </p>
          <input type="submit"/>
        </form>"""

    token = get_token(request)
    response=response.replace('__token__',html.escape(token))

    response+= dumpdata('POST',request.POST)
    return HttpResponse(response)