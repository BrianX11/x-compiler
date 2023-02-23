import re

arithmetic_operators = {
    "ADD": "+",
    "SUB": "-",
    "MUL": "*",
    "DIV": "/",
    "MOD": "%",
    "EXP": "**",
    "ASS": "="
}

comparison_operators = {
    "EQUAL": "==",
    "NOT_EQUAL": "!=",
    "GREATER": ">",
    "LESS": "<",
    "E_GREATER": ">=",
    "E_LESS": "<="
}

logical_operators = {
    "AND": "&&",
    "OR": "||",
    "NOT": "!"
}

def isOperator(input):
    for key, value in {**arithmetic_operators, **comparison_operators, **logical_operators}.items():
        if re.search("^" + re.escape(value)  + "$", input):
            return key
    return False