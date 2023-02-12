import re

delimiters = {
    "L_BRACKET": "{",
    "R_BRACKET": "}",
    "L_PAREN": "(",
    "R_PAREN": ")",
    "L_SQUARE_BRACKET": "[",
    "R_SQUARE_BRACKET": "]",
    "COMMA": ",",
    "SEMICOLON": ";",
    "QUOTE": "'",
    "DOUBLE_QUOTE": "\"",
    "BACKSLASH": "\\",
    "SLASH": "/",
    "COLON": ":",
    "DOT": ".",
}

def isDelimiter(input):
    for key, value in delimiters.items():
        if re.search("^" + value + "$", input):
            return key
    return False