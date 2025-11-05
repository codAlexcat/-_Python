# Задание 1
def list_user(listing):
    if not listing:
        return None
    min_index = 0
    min_value = listing[0]
    for i in range(1, len(listing)):
        if listing[i] < min_value:
            min_value = listing[i]
            min_index = i
    return min_index

numbers = [4, 5, 2, 7, 1, 9, 8]
print(f"Индекс минимального элемента: {list_user(numbers)}")

# Задание 2
def numbers_list(n):
    a = n.split(" ")
    a.sort()
    b = str(a)
    print(b)

numbers = input("Введите числа через пробел: ")
numbers_list(numbers)