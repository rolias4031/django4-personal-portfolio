from django.shortcuts import render
from django.http import HttpResponse
import operator
from .calc_funcs import *

def calculator(request):
    """
    - this calculator works by processing individual inputs from the user. each key possibility fits into an option in the if/elif tree below. from there, specific functions govern the calculators behavior.

    - the calculator uses 3 distinct modes kept in the Data class (Data.modes) to further specify which inputs should work at any given point in the calculation process. those modes: 'first_num','operator','second_num'. the Data class is imported from calc_funcs.py
    """

    if request.GET: #wait for request.GET to return True before starting program logic

            r = request.GET #store request.GET object as r
            char = list(r.values())[0] #extract the specific string character to operate on
            print(r)

            if char in Data.numbers: #checks if char is a digit 0-9 or a decimal

                if Data.mode == "first_num": #uses Data.mode to determine where char should be used
                    create_number(char, Data)

                elif ((Data.mode == "operator") and (len(Data.session_data['operator']) > 0)) or (Data.mode == "second_num"):
                    Data.mode = "second_num"
                    create_number(char, Data)

            elif char in Data.ops.keys(): #checks if char is an operator

                if (Data.mode == "first_num") or (Data.mode == "operator"):
                    get_operator(r, Data)

                elif (Data.mode == "second_num"):#an operator key after second_num acts as the equals button

                    if number_check(Data): #checks for illegitimate number builds before calculation
                        return

                    calculate(Data) #core calculation logic
                    get_operator(r, Data)
                    Data.session_data['display_num'] = Data.session_data['first_num']

            elif (char == "=") and (Data.mode == "second_num"): #check for an equals input and proper mode
                calculate(Data)

            elif char == "%":
                convert_to_percentage(Data)

            elif (char == "±") and (Data.mode in ['first_num','second_num']):
                sign_change(Data)

            elif char == "AC": #checks for clear input to wipe calculators Data.session_data
                clear_calc(Data)


    return render(request, 'calculator/calculator.html', {'display_num':Data.session_data['display_num']})
