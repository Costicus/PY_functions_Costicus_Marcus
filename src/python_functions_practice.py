def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    return a / b 

def length_of_string(string):
    return len(string)

def join_string(string_1, 
string_2):
    return string_1 + string_2

def add_string_as_number(a, b):
    string_number = int(a) + int(b)
    return string_number

def number_to_full_month_name(month):
    if month == 1:
        return "January" 
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    else:
        return "December"


def number_to_short_month_name(month):
    if month == 1:
        return "Jan" 
    elif month == 2:
        return "Feb"
    elif month == 3:
        return "Mar"
    elif month == 4:
        return "Apr"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "Aug"
    elif month == 9:
        return "Sept"
    elif month == 10:
        return "Oct"
    elif month == 11:
        return "Nov"
    else:
        return "Dec"

def volume_of_cube(length, width, height):
    return length * width * height

def reverse_string(string):
    list_string = list(string)
    list_string.reverse()
    val = ''.join(list_string)
    return val

def fahrenheit_to_celsius(a):
    return a - a * 9/5 + 32