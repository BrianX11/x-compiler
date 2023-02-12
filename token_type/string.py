import re

string_pattern = r'"(.*?)"'

def isString(input):
    if re.search(string_pattern, input):
        return "String"
    return False