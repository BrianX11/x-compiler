from token_type.keyword import isKeyword
from token_type.delimiter import delimiters, isDelimiter
from token_type.operator import isOperator
from token_type.identification import isID
from token_type.number import isNumber
from token_type.string import isString

source_code = open("example.x", "r")
line = "None"

tokens = ("", "")
pattern = ""
lexeme = ""

while line:
    line = source_code.readline()

    pos = 0
    temp = ""

    while pos < len(line):

        current = line[pos]

        if not (isDelimiter(current) or isOperator(current)) and not (isDelimiter(temp) or isOperator(temp)) and current != '\n':
            temp += current
            pos += 1
        else:
            if temp: 
                if (isOperator(temp)) and (isOperator(current)):
                    temp += current
                    pos += 1
                    continue

                keyword = isKeyword(temp)
                _id = isID(temp)
                number = isNumber(temp)
                delimiter = isDelimiter(temp)
                operator = isOperator(temp)

                if keyword:
                    print((temp, "KEYWORD", keyword))
                elif _id:
                    print((temp,"ID", _id))
                elif number:
                    print((temp,"NUMBER", number))
                elif delimiter and not temp==delimiters["WHITESPACE"]:
                    print((temp,"DELIMITER", delimiter))
                elif operator:
                    print((temp,"OPERATOR", operator))
                temp = ""
            else:
                temp += current
                pos += 1


            