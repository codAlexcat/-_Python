from operations import add, division, multiplication, subtraction

# определения нужной операции
def operation(a, b, oper):
    if oper == "+":
        return add.add(a, b)
    elif oper == "-":
        return subtraction.minus(a, b)
    elif oper == "*":
        return multiplication.multiplication(a, b)
    elif oper == "/":
        return division.division(a, b)
