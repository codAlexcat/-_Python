def UPPER(string):
    return string.upper()

def LEN(string):
    return len(string)

def POL(string):
    if string == string[::-1]:
        return True
    return False