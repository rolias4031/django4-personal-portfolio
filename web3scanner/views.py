import json
from django.shortcuts import render
from web3 import Web3
from .web3_package.scanner_utils import *

# Create your views here.
def scanner(request):

    token_data = {}
    error_msg = None

    if request.GET.get('Submit'): #check for a submission, run the function associated with that token name

        token = request.GET.get('Token')

        try:
            token_data = credentials[token]['function'](token_data, credentials[token])
            error_msg = None

        except KeyError:
            error_msg = 'That token needs some work... select another.'
            token_data = {}

    return render(request, 'web3scanner/scanner.html', {'token_data':token_data,'error_msg':error_msg})
