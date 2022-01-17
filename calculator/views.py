from django.shortcuts import render
from django.http import HttpResponse
import operator
from .calc_funcs import *
from time import sleep

def calculator(request):

    if request.GET: #wait for request.GET to return True before starting while loop

            r = request.GET #store request.GET object as r

            print(r)

            char = list(r.values())[0]

            if char in Data.numbers:

                create_number(char, Data)

            elif char in Data.ops.keys():

                if Data.i == "1":

                    op, Data.i = get_operator(r, Data)

            elif (char == "=") and (Data.i == "2"):

                calculate(Data)

            elif (char == "AC"):

                clear_calc(Data)


    return render(request, 'calculator/calculator.html')
