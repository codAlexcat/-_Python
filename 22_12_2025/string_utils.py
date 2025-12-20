
# Палиндром
def Palindrome(string):
    if string == string[::-1]:
        return f"Строка {string} является палиндромом"
    return f"Строка {string} не является палиндромом"

# анаграмма
def Anagram(s1, s2):
    if len(s1) != len(s2):
        return "эти строки не являются анаграммой"

    s2_list = list(s2)  # Превращаем в список, чтобы можно было удалять буквы

    for char in s1:
        if char in s2_list:
            s2_list.remove(char)  # Удаляем одну найденную букву
        else:
            return "эти строки не являются анаграммой"  # Если буквы нет выход

    return "Эти строки являются анаграммой ^_^ "

# Перевертыш
def turn_over(string):
    return string[::-1]

