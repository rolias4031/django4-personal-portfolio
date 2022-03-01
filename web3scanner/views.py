import json
from django.shortcuts import render
from web3 import Web3
from .web3_package.scanner_utils import *
import cryptocompare as cc

#class to hold the web3 connection objects
class Conn():
    web3, connect_bool = web3_connect()

def scanner(request):

    #check for a submission, run the function associated with that token name
    if request.GET.get('token_submit') and Conn.connect_bool:

        Creds.current_token = request.GET.get('Token')

        try:
            Creds.token_data = Creds.credentials[Creds.current_token]['function'](Conn.web3, Creds.token_data, Creds.credentials[Creds.current_token])
            creds_reset(wallet_bool=True, error_bool=True)

        except KeyError:
            Creds.error_msg = 'That token needs some work... select another.'
            creds_reset(token_bool=True)

    elif request.GET.get('address_submit') and Conn.connect_bool:

        Creds.wallet_data['address'] = request.GET.get('address_field')

        try:
            Creds.wallet_data['balance'], Creds.wallet_data['percent_supply'] = fetch_address_balance(Conn.web3, Creds.wallet_data['address'], Creds.token_data, Creds.credentials[Creds.current_token])
            creds_reset(error_bool=True)

        except ValueError:
            Creds.error_msg = "That's not a valid address"
            creds_reset(wallet_bool=True)

    elif Conn.connect_bool == False:
        Creds.error_msg = 'Web3 Connection Failed'

    return render(request, 'web3scanner/scanner.html', {'token_data':Creds.token_data, 'wallet_data':Creds.wallet_data, 'error_msg':Creds.error_msg,'current_token':Creds.current_token})
