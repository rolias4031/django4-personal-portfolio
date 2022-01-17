from django.shortcuts import render
from django.http import HttpResponse
from PyDictionary import PyDictionary
from . import dict_funcs

# Create your views here.
def dictionary(request):

    dictionary = PyDictionary()

    # definitions = None
    # synonyms = None
    # antonyms = None
    # errormsg = None

    the_word = request.GET.get('the_word')

    try:
        definitions = dictionary.meaning(the_word)
        synonyms = [x.capitalize() for x in dict_funcs.synonyms(the_word)]
        antonyms = [x.capitalize() for x in dict_funcs.antonyms(the_word)]
        errormsg = None

        if definitions:
            for key, value in definitions.items():
                for i in range(0, len(value)):
                    value[i] = value[i].split(" ")
                    value[i][0] = value[i][0].capitalize()
                    definitions[key][i] = " ".join(value[i])

        if the_word == '':
            errormsg = 'Enter a word'

        if definitions is None:
            errormsg = 'Word not found'

    except AttributeError:
        definitions, synonyms, antonyms, errormsg = None, None, None, None
        the_word = ''

    return render(request, 'dictionary/dictionary.html', {'the_word':the_word, 'definitions':definitions, 'synonyms':synonyms, 'antonyms':antonyms, 'errormsg':errormsg, 'x':type(definitions), 'thesaurus':{'synonyms':synonyms, 'antonyms':antonyms}})
