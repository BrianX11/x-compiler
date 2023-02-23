from token_type.keyword import isKeyword
from token_type.delimiter import delimiters, isDelimiter
from token_type.operator import isOperator
from token_type.identification import isID
from token_type.number import isNumber
from token_type.string import isString, isStringStart

source_code = open("example.x", "r")
line = "None"

tokens = ("", "")
pattern = ""
lexeme = ""

for line in source_code:
    temp = ""
    for pos, current in enumerate(line):
        if isDelimiter(current) or isDelimiter(temp):
            if temp:
                if isOperator(temp+current) or isStringStart(temp):
                    temp += current
                else:
                    token_type = (
                        ("KEYWORD", isKeyword(temp)),
                        ("ID", isID(temp)),
                        ("NUMBER", isNumber(temp)),
                        ("STRING", isString(temp)),
                        ("OPERATOR", isOperator(temp)),
                        ("DELIMITER", isDelimiter(temp)),
                        ("UNKNOWN", None)
                    )
                    token = next((t for t in token_type if t[1]), token_type[-1])
                    if temp != delimiters["WHITESPACE"]:
                        print((temp, token[0], token[1]))
                    temp = current
            else:
                temp += current
        else:
            temp += current
        

            