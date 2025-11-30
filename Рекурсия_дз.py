# задача 2
def num(n, list=[]):
     if n == 0:
         print(list)
         return
     for i in range(1, n + 1):
         list.append(i)
         num(n - i, list)
         list.pop()

try:
    n = int(input("Введите число: "))
except:
    print("Это не число!")
    n = int(input("Введите число!: "))

num(n)


# задача 1
"""
Нахождение наибольшего элемента в списке
Реализуйте функцию, которая рекурсивно
находит наибольший элемент в списке.
"""

def max_list(num):
    if len(num) == 1:
        return num[0]

    rest_max = max_list(num[1:])  # убираем первый элемент
    return num[0] if num[0] > rest_max else rest_max

numbers = [3, 7, 2, 9, 1, 8]
print(f"Максимум: {max_list(numbers)}")