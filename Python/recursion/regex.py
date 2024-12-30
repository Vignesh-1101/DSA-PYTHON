import re
def is_valid_regex(regex, value):
    try:
        if re.match(regex, value):
            return True
        else:
            return False
    except re.error:
        return False
    
    # r"^[A-Za-z]+(?:[\s.][A-Za-z]+)*$"
    # r"^[A-Za-z]+(?:\\s*\\.\\s*[A-Za-z]+)*$"
    # "^[A-Za-z]+\\.\\s+[A-Za-z]+(?:\\s+[A-Za-z]+)*$"
    # "^[A-Za-z]+(?:\\.\\s?[A-Za-z]+)*$"
    # "^(?:Dr\\.?\\s*)?(?:[A-Za-z](?:\\.?\\s*)?)+$"
print(is_valid_regex("^[A-Za-z]+(?:[\\s.][A-Za-z]+)*$", "hss.wq21"))  # True