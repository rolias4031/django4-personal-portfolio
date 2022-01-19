from django.shortcuts import render
from django.http import HttpResponse
import operator

class Data:
    """
    class that holds all calculator data.
    """
    mode = "first_num" #the current mode of the calculator ('first_num','second_num','operator')

    #the calculator's data for the current calculation, accessed through Data.session_data[key]
    session_data = {'first_num':'','second_num':'','operator':'','final_num':'','display_num':''}

    numbers = ["."] + [str(x) for x in range(0,10)] #the list of valid integers the calculator accepts

    #dictionary of operator symbols and their respective functions
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "×": operator.mul,
        "÷": operator.truediv
        }

    #list of other symbols that the calulator accepts
    symbols = ["=","%",".","±"]

def create_number(digit, Data):
    """
    takes a digit and adds it to the number that corresponds with the current Data.mode
    """
    #quick check to ensure only 1 decimal is present in any number at any time.
    if (digit == ".") and (list(Data.session_data[Data.mode]).count(".") == 1):
        return

    Data.session_data[Data.mode] += digit #append that value to the list at "1" in session_data dictionary
    Data.session_data['display_num'] = Data.session_data[Data.mode] #updates calculator display

    # print(f'digit = {digit}')
    # print(f'session_data = {Data.session_data}')
    # print(f'mode = {Data.mode}')

    return

def get_operator(r, Data):
    """
    takes an operator symbol and sets it as the current operator and changes the Data.mode to "operator". before doing this, runs a number_check() and decimal_check() to clean up numbers and catch invalid inputs.
    """

    if number_check(Data): #prevents a solo "." from passing as a number input
        return

    if Data.mode in ['first_num','second_num']:
        decimal_check(Data) #function that adds "0" if first or last char in number is "." before moving into "operator" mode

    Data.session_data['operator'] = list(r.values())[0] #store specific operator char
    Data.mode = "operator"

    # print(f'{Data.session_data}')
    # print(f'mode = {Data.mode}')

    return

def calculate(Data):
    """
    calculates a 'final_num' from the Data.session_data. runs a number_check() and a decimal_check() prior to prevent invalid inputs. after, calls format_calc_output() to convert the 'final_num' int or float into presentable string for 'display_num'. then calls calc_admin() to reconfigure Data.session_data for a new calculation.

    after a calculation, the calculator moves directly into 'operator' mode, not 'first_num', because it uses the most recent 'final_num' as the 'first_num' for the new calculation. this allows the user to progressively build on their calculations.
    """

    if number_check(Data):
        return

    decimal_check(Data)

    #--- begin main calculation process ---
    operation_func = Data.ops[Data.session_data['operator']] #the operation function from ops dictionary with 'operator' key
    first_num, second_num = convert_from_str(Data)
    num = operation_func(first_num, second_num)

    format_calc_output(num, Data)
    #--- end main calculation process ---

    calc_admin(Data) #reconfigure Data.session_data for a new session

    # print(f'{Data.session_data}')
    # print(f'mode = {Data.mode}')

    return

def clear_calc(Data):
    """
    clears the calculator's Data.session_data after detecting am "AC" input at any point in the current session
    """

    Data.session_data = {key: '' for key in Data.session_data} #dictionary comprehension to reset session_data
    Data.mode = "first_num" #resets mode to 'first_num'

    # print(f'{Data.session_data}')
    # print(f'mode = {Data.mode}')

    return

def convert_from_str(Data):
    """
    takes the 'first_num','second_num' strings in Data.session_data and converts them into their respective number types, then returns them to be used in calculate()
    """

    for x in ['first_num','second_num']:
        try:
            Data.session_data[x] = int(Data.session_data[x])
        except ValueError:
            Data.session_data[x] = float(Data.session_data[x])

    first_num, second_num = Data.session_data['first_num'], Data.session_data['second_num']

    return first_num, second_num

def convert_to_percentage(Data):
    """
    takes the display_num and converts it to a percentage immediately when the "%" button is pushed
    """

    Data.session_data['display_num'] = str(float(int(Data.session_data['display_num'])/100))
    return

def decimal_check(Data):
    """
    checks if the number for the current Data.mode contains a deciaml, then appends a 0 before or after that decimal to avoid illegitimate numbers, then updates the display_num to reflect that change.
    """

    if "." in Data.session_data[Data.mode]:
        if (Data.session_data[Data.mode].index(".") == 0):
            Data.session_data[Data.mode] = "0" + Data.session_data[Data.mode]

        elif (Data.session_data[Data.mode].index(".") == len(Data.session_data[Data.mode]) - 1):
            Data.session_data[Data.mode] = Data.session_data[Data.mode] + "0"

    Data.session_data['display_num'] = Data.session_data[Data.mode]

    return

def number_check(Data):
    """
    checks if number at current Data.mode is a single ".", and returns True if that stement is True, which prevents the functon it is nested in from moving forward with a bad input.
    """

    if (len(Data.session_data[Data.mode]) == 1) and ("." in Data.session_data[Data.mode]):
        return True

def calc_admin(Data):
    """
    reconfigure Data.session_data for a new calculation. changes 'first_num' to 'final_num' and Data.mode to 'operator' because we want the user to be able to build on their previous calculation. the equals sign essentially calculates the number and then skips Data.mode  = 'first_num'
    """
    Data.session_data['display_num'] = Data.session_data['final_num'] #set the display_num to final_num
    Data.session_data['first_num'] = Data.session_data['final_num']
    Data.session_data['second_num'] = ''
    Data.session_data['operator'] = ''
    Data.mode = "operator"

    return

def format_calc_output(num, Data):
    """
    formts the 'final_num' into a presentable string for 'display_num'. checks if a decimal is in num, and then counts the number of characters after the decimal to determine the number of decimal places. uses that len() in .format(num) to avoid unneccessary decimals with a max of 6 decimals for any number.
    """

    if "." in str(num):

        decimal_places = len(str(num).split(".")[1])

        if decimal_places < 6:
            format_str = "{:." + str(decimal_places) + "f}"
        else:
            format_str = "{:.6f}"

        Data.session_data['final_num'] = format_str.format(num)

    else:

        Data.session_data['final_num'] = str(num)

    return

def sign_change(Data):
    """
    adds or removes a "-" to the current number when the pos-neg button is pushed.
    """

    if "-" in Data.session_data[Data.mode]:
        Data.session_data[Data.mode] = Data.session_data[Data.mode][1:]

    elif "-" not in Data.session_data[Data.mode]:
        Data.session_data[Data.mode] = "-" + Data.session_data[Data.mode]

    Data.session_data['display_num'] = Data.session_data[Data.mode]

    return
