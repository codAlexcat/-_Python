
# Функция для вычисления факториала числа
def Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Функция для вычисления фибоначчи
def Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Функция для вычисления суммы цифр заданного числа
def Summa(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result








