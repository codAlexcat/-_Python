import random

def rand_num():
    n1 = int(input("Введите первое число: "))
    n2 = int(input("Введите второе число: "))
    print(random.randint(n1, n2))

def rand_list():
    num = int(input("Введите нужное количество символов: "))
    list1 = [ random.randint(1, 100) for _ in range(num) ]
    print(list1)

def SHUFFLE(list1):
    random.shuffle(list1)
    print(list1)