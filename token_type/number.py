import re

number_pattern = r"^\d*\.?\d*$"

def isNumber(input):
    if re.search(number_pattern, input):
        return "Number"
    return False