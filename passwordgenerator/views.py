from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
def generator(request):

    the_password = None
    characters = list(string.ascii_lowercase)

    if request.GET.get('Uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*?'))

    length = int(request.GET.get('length', 21))

    if request.GET.get('Generate'):
        the_password = ''
        for i in range(length):
            the_password += random.choice(characters)

    return render(request,'passwordgenerator/pw_generator.html', {'the_password': the_password})
