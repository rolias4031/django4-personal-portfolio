from django.shortcuts import render
from django.http import HttpResponse
import operator

class Data:
    i = "1"
    session_data = {'1':'','2':'','op':''}
    numbers = [str(x) for x in range(0,10)]
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "×": operator.mul,
        "÷": operator.truediv
        }
    symbols = ["=","."]

class Number():

    def __init__(self):

        self.digits = ''

    def add_digit(self, digit):

        self.digits += digit


def input_triage(r, i, numbers, ops, session_data):

    if list(r.values())[0] in numbers:

        return create_number(r, i, session_data)

    elif list(r.values())[0] in ops:

        if (i == "1") or (i == "2"):

            return get_operator(r, i)

        elif i == "3":
            pass

def create_number(digit, Data):

    Data.session_data[Data.i] += digit #append that value to the list at "1" in session_data dictionary

    print(f'digit = {digit}')
    print(f'session_data = {Data.session_data}')

    return Data.session_data

def get_operator(r, Data):

    Data.session_data['op'] = list(r.values())[0]
    Data.i = "2"

    print(f'{Data.session_data["op"]}, {Data.i}')

    return Data.session_data, Data.i

def calculate(Data):

    calculated_num = Data.ops[Data.session_data['op']](int(Data.session_data['1']), int(Data.session_data['2']))
    Data.session_data['1'] = calculated_num
    Data.i = "1"
    print(calculated_num)

def clear_calc(Data):

    Data.session_data = {key: '' for key in Data.session_data}
    Data.i = "1"

    print(f'{Data.session_data}, {Data.i}')

    return Data.session_data, Data.i

def switchboard():
    pass
