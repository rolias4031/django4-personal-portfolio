import json
from web3 import Web3
from .scanner_credentials import *


def fetch_func_one(token_data, token_creds):

        web3, connect_bool = web3_connect() #get web3 connection, only do something if connect_bool is True

        if connect_bool:

            abi = json.loads(token_creds['abi'])
            contract = web3.eth.contract(address=token_creds['contract'], abi=abi)

            token_funcs = {
                'Name': contract.functions.name,
                'Symbol': contract.functions.symbol,
                'Total Supply': contract.functions.totalSupply,
                'Decimals': contract.functions.decimals
                }

            token_data = {key: value().call() for (key, value) in token_funcs.items()}
            token_data['is_connected'] = True
            token_data['Contract Address'] = token_creds['contract']

            totalsupply_format(token_data)

            return token_data

def tether_fetch(token_data):

    if web3_connect():

        token_data['is_connected'] = True
        token_data['token_name'] = "Tether"

def web3_connect():
    web3 = Web3(Web3.HTTPProvider(infura))
    return web3, web3.isConnected()

def totalsupply_format(token_data):

    decimals = str(token_data['Total Supply'])[-token_data['Decimals']:]

    index = len(str(token_data['Total Supply'])) - token_data['Decimals']
    whole_nums = "{:,}".format(int(str(token_data['Total Supply'])[:index]))

    token_data['Total Supply'] = whole_nums + "." + decimals

    return


#dictionary that holds the functions for each token and the credentials for each token. key must match the string used in the dropdown menu in the interface.
credentials = {
    'OMG':{'function':fetch_func_one, 'contract': omg_contract, 'abi':omg_abi},
    'Tether':{'function':fetch_func_one, 'contract': tether_contract, 'abi':tether_abi},
    'Shiba Inu':{'function':fetch_func_one, 'contract': shiba_inu_contract, 'abi': shiba_inu_abi},
    'BNB':{'function':fetch_func_one, 'contract':bnb_contract, 'abi': bnb_abi},
    'HEX':{'function':fetch_func_one, 'contract':hex_contract, 'abi': hex_abi},
    'Wrapped BTC':{'function':fetch_func_one,'contract':wrapped_btc_contract,'abi':wrapped_btc_abi},
    'Chainlink':{'function':fetch_func_one,'contract':chainlink_contract,'abi':chainlink_abi},
    'Fantom':{'function':fetch_func_one,'contract':fantom_contract,'abi':fantom_abi}
    }

infura = 'https://mainnet.infura.io/v3/25d9ebfebc264defaf34b9fa1d6e217b'
