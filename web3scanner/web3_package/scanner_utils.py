import json
from web3 import Web3
from .scanner_credentials import *

def fetch_token_stats(web3, token_data, token_creds):

    abi = json.loads(token_creds['abi'])
    contract = web3.eth.contract(address=token_creds['contract'], abi=abi)

    token_funcs = {
        'Name': contract.functions.name,
        'Symbol': contract.functions.symbol,
        'Total Supply': contract.functions.totalSupply,
        'Decimals': contract.functions.decimals
        }

    token_data = {key: value().call() for (key, value) in token_funcs.items()}
    token_data['Contract Address'] = token_creds['contract']

    token_data['Total Supply'] = format_number(token_data['Total Supply'], token_data)

    return token_data

def fetch_address_balance(web3, address, token_data, token_creds):

    abi = json.loads(token_creds['abi'])
    contract = web3.eth.contract(address=token_creds['contract'], abi=abi)

    raw_wallet_balance = contract.functions.balanceOf(Web3.toChecksumAddress(address)).call()

    wallet_balance = format_number(raw_wallet_balance, token_data)

    percent_totalsupply = round(((float(wallet_balance.replace(",","")))/(float(token_data['Total Supply'].replace(",",""))))*100, 3)

    return wallet_balance, percent_totalsupply

def creds_reset(token_bool=False, wallet_bool=False, error_bool=False):
    if token_bool:
        Creds.token_data = {}
    if wallet_bool:
        Creds.wallet_data = {key:None for key in Creds.wallet_data.keys()}
    if error_bool:
        Creds.error_msg = None

def web3_connect():
    web3 = Web3(Web3.HTTPProvider(Creds.infura_url))
    return web3, web3.isConnected()

def format_number(num_format, token_data):

    decimals = str(num_format)[-token_data['Decimals']:]

    index = len(str(num_format)) - token_data['Decimals']
    whole_nums = "{:,}".format(int(str(num_format)[:index]))

    num_format = whole_nums + "." + decimals

    return num_format

#dictionary that holds the functions for each token and the credentials for each token. key must match the string used in the dropdown menu in the interface.
class Creds:
    token_data = {}
    wallet_data = {
        'address': None,
        'balance': None,
        'percent_supply': None,
        }
    credentials = {
        'OMG':{'function':fetch_token_stats, 'contract': omg_contract, 'abi':omg_abi},
        'Tether':{'function':fetch_token_stats, 'contract': tether_contract, 'abi':tether_abi},
        'Shiba Inu':{'function':fetch_token_stats, 'contract': shiba_inu_contract, 'abi': shiba_inu_abi},
        'BNB':{'function':fetch_token_stats, 'contract':bnb_contract, 'abi': bnb_abi},
        'HEX':{'function':fetch_token_stats, 'contract':hex_contract, 'abi': hex_abi},
        'Wrapped BTC':{'function':fetch_token_stats,'contract':wrapped_btc_contract,'abi':wrapped_btc_abi},
        'Chainlink':{'function':fetch_token_stats,'contract':chainlink_contract,'abi':chainlink_abi},
        'Fantom':{'function':fetch_token_stats,'contract':fantom_contract,'abi':fantom_abi}
        }
    infura_url = 'https://mainnet.infura.io/v3/25d9ebfebc264defaf34b9fa1d6e217b'
    current_token = None
    error_msg = None
