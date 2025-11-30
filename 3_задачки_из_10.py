# №1
from os import remove

print("_" * 130)
print("№1")
list1 = [3, 6.5, 34, 7, "Hi", 5, "Привет", True]
now_list = []
# добавляем в список "now_list" только числа
for i in list1:
    if isinstance(i, (int, float)) and not isinstance(i, (bool)):
        now_list.append(i)
# считаем и выводим сумму
print(sum(now_list))

# №2
print("_" * 130)
print("№2")
list2 = [0, 1, 2, 3, 5]
# получаем от пользователя делитель с исключением ошибки
try:
    num_user = int(input("Введите делитель: "))
except:
    print("Вы ввели не число! ")
    num_user = int(input("Введите делитель: "))
# делим все добавляя в новый список
now_list1 = []
for i in list2:
    # на 0 делить нельзя поэтому просто добавим его в новый список
    if i == 0:
        now_list1.append(i)
    else:
        now_list1.append(i / num_user)

print(now_list1)
if 0 in list2:
    print("В списке числителей был ноль, а по скольку 0 нельзя делить не на что, я добавил его в новый список просто так ^_^")

# №3
print("_" * 130)
print("№3")
list3 = []
list4 = [2, 4, 8, 2, 12]
try:
    print(f"Первый список: {max(list3)}")
except:
    print("Первый список пустой :( ")

try:
    print(f"Второй список: {max(list4)}")
except:
    print("Второй список тоже пустой :( ")

# №4
print("_" * 130)
print("№4")
list5 = [1, 2, 3, "я", "вы"]
user = input("Введите элемент который хотите найти в списке: ")

try:
    user1 = int(user)
    if user1 in list5:
        print(f"Да в списке есть элемент '{user1}'")
    else:
        print(f"Элемента '{user1}' нету в списке")
except:
    if user in list5:
        print(f"Да в списке есть элемент {user}")
    else:
        print(f"Элемента '{user}' нету в списке")

# №5
print("_" * 130)
print("№5")
list6 = ["банан", "яблоко", "киви", "арбуз", "манго"]
user_string = input("Введите строку которую хотите удалить из списка: ")
try:
    list6.remove(user_string)
    print(f"Строка '{user_string}' была удалена из списка")
except ValueError:
    print("Такой строки в списке нету ")





