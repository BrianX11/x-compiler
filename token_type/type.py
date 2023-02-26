import re

number_pattern = r"^\d*\.?\d*$"

string_pattern = r'"(.*?)"'
string_start = r'"(.*?)+'

def isNumber(input):
    if re.search(number_pattern, input):
        return "Number"
    return False

def isString(input):
    if re.search(string_pattern, input):
        return "String"
    return False

def isStringStart(input):
    if re.search(string_start, input) and not isString(input):
        return "String"
    return False