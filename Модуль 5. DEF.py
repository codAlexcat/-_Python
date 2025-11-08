# # Задание 1
# def display_quote(text, author):
#     print(f"<{text}>\n{" " * 65}{author}")
#
# text = "Don t let the noise of others opinions drown out your own inner voice."
# author = "Steve Jobs"
#
# display_quote(text, author)
#
# # Задание 2
# def odd_numbers(num1,  num2):
#     if num1 > num2:
#         num1, num2 = num2, num1
#     for i in range(num1, num2 + 1):
#         if i % 2 != 0:
#             print(i)
#
# odd_numbers(9, 1)
#
# # Задание 3
# def line(length, direction, symbol):
#     if direction == 1:
#         print(symbol * length)
#     elif direction == 2:
#         for i in range(length):
#             print(symbol)
#
# length_user = int(input("Введите длину линии: "))
# direction_user = int(input("Выберите направление, 1 - горизонталь, 2 - вертикаль: "))
# symbol_user = input("Введите символ: ")
# line(length_user, direction_user, symbol_user)
#
#
# # Задание 4
# def maximum(num1, num2, num3, num4):
#     max_num = max(num1, num2, num3, num4)
#     print(max_num)
#
# maximum(1, 4, 8, 2)
#
# # Задание 5
# def summator(a, b):
#     if a > b:
#         a, b = b, a
#     summa = 0
#     for i in range(a, b + 1):
#         summa += i
#     print(summa)
#
# summator(10, 5)
#
# # Задание 6
# import math
#
# def prime_number(num):
#   if num <= 1:
#     return False
#
#   for i in range(2, int(math.sqrt(num)) + 1):
#     if num % i == 0:
#       return False
#
#   return True
#
# number = int(input("Введите число: "))
# if prime_number(number):
#   print(f"{number} — простое число")
# else:
#   print(f"{number} — составное число")

# Задание 7
def happy(num):
    summa_1 = 0
    for i in range(3):
        summa_1 += int(num[i])
    summa_2 = 0
    for i in range(3, 6):
        summa_2 += int(num[i])
    if summa_1 == summa_2:
        return True
    else:
        return False


user_num = input("Введите шестизначное число: ")
if happy(user_num):
    print(f"{user_num} - Счастливое число! ураааааа)")
else:
    print(f"{user_num} - не счастливое число, оно грустит(")

