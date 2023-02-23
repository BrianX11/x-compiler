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
    "COLON": ":",
    "WHITESPACE": " ", 
}

def isDelimiter(input):
    for key, value in delimiters.items():
        if re.search("^" + re.escape(value) + "$", input):
            return key
    return False

