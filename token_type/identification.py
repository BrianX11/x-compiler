import re
from token_type.keyword import isKeyword

_id_pattern = r"^(?!\d)[a-zA-Z\d_]+"

def isID(input):
    if re.search(_id_pattern, input) and not isKeyword(input):
        return "ID"
    return False