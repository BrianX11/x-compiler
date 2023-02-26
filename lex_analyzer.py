from token_type.keyword import isKeyword
from token_type.delimiter import delimiters, isDelimiter
from token_type.operator import isOperator
from token_type.identification import isID
from token_type.type import isNumber, isString, isStringStart

class Token:
    class Attr:
        def __init__(self, line, start_pos, end_pos):
            self.line = line
            self.start_pos = start_pos
            self.end_pos = end_pos

    def __init__(self, type, token, lexeme, attributes=None):
        self.type = type
        self.token = token
        self.lexeme = lexeme
        self.attributes = attributes if attributes is not None else Token.Attr(None, None, None)
    
    token_type = (
        ("KEYWORD", isKeyword),
        ("ID", isID),
        ("NUMBER", isNumber),
        ("STRING", isString),
        ("OPERATOR", isOperator),
        ("DELIMITER", isDelimiter),
        ("UNKNOWN", None)
   )
    
    @classmethod
    def append(cls, tokens_list, lexeme, line, start, end):
        attributes = cls.Attr(line, start, end)
        token_type = next((t for t in cls.token_type if t[1](lexeme)), cls.token_type[-1])
        new_token = cls(token_type[0], token_type[1], lexeme, attributes)
        tokens_list.append(new_token)

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
                        if temp != delimiters["WHITESPACE"]:
                            Token.append(tokens, temp, line_n, start, pos)
                        start = pos
                        temp = current
                else:
                    temp += current
            else:
                temp += current
    return tokens

            