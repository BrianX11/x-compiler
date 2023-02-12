import re

keywords = {
    "CONDITIONAL_IF": "if",
    "CONDITIONAL_ELIF": "elif",
    "CONDITIONAL_ELSE": "else",
    "LOOP_FOR": "for",
    "LOOP_WHILE": "while",
    "RETURN": "return",
    "FUNCTION": "function",
    "BREAK": "break",
    "CONTINUE": "continue",
    "GOTO": "goto",
}

types = {
##    "INTEGER": "int",
##    "FLOAT": "float",
    "NUMBER": "num",
    "STRING": "string"
}

def isKeyword(input):
    for key, value in {**keywords, **types}.items():
        if re.search("^" + value + "$", input):
            return key
    return False