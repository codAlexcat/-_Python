# Функция по сложению
def add(a, b):
    if type(a) != int and type(b) != int:
        return "a и b не являются числом!"
    else:
        result = a + b
        return result
