import re

string_pattern = r'"(.*?)"'
string_start = r'"(.*?)+'


def isString(input):
    if re.search(string_pattern, input):
        return "String"
    return False

def isStringStart(input):
    if re.search(string_start, input):
        return "String"
    return False