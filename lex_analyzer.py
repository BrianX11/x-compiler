from token_type.keyword import isKeyword
from token_type.delimiter import delimiters, isDelimiter
from token_type.operator import isOperator
from token_type.identification import isID
from token_type.type import isNumber, isString, isStringStart

def parse(input):
    tokens=[]
    line_n = 0
    for line_n, line in enumerate(input):
        temp = ""
        start = 0
        for pos, current in enumerate(line + ' '):
            if isDelimiter(current) or isDelimiter(temp):
                if temp:
                    if isOperator(temp+current) or isStringStart(temp):
                        temp += current
                    else:
                        token_type = (
                            ("KEYWORD", isKeyword(temp), "cyan"),
                            ("ID", isID(temp), "yellow"),
                            ("NUMBER", isNumber(temp), "green"),
                            ("STRING", isString(temp), "green"),
                            ("OPERATOR", isOperator(temp), "red"),
                            ("DELIMITER", isDelimiter(temp), "magenta"),
                            ("UNKNOWN", None)
                        )
                        token = next((t for t in token_type if t[1]), token_type[-1])
                        if temp != delimiters["WHITESPACE"]:
                            tokens.append((temp, token[0], token[1], start, pos, line_n, token[2]))
                            print((temp, token[0], token[1], start, pos, line_n))
                        start = pos
                        temp = current
                else:
                    temp += current
            else:
                temp += current
    return tokens

            