import re

_id_pattern = r"^(?!\d)[a-zA-Z\d_]+"

def isID(input):
    if re.search(_id_pattern, input):
        return "ID"
    return False