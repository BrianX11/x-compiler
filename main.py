from token_type.keyword import isKeyword
from token_type.delimiter import isDelimiter
from token_type.operator import isOperator
from token_type.identification import isID
from token_type.number import isNumber
from token_type.string import isString

source_code = open("example.x", "r")
line = "None"

while line:
    line = source_code.readline()

