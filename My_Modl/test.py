# String_utils.py
from string_utils import UPPER, LEN, POL
string = "дед"
print("Преобразование строки в верхний регистр")
print(UPPER(string))
print("Подсчет количества символов в строке.")
print(LEN(string))
print("Проверка, является ли строка палиндромом")
print(POL(string))

# random_utils.py
from random_utils import rand_num, rand_list, SHUFFLE
print("Генерация случайного целого числа в заданном диапазоне")
rand_num()
print("Генерация случайного списка из заданного количества элементов")
rand_list()
print("Перемешивание элементов списка")
my_list = [1, 4, 2, 5 ,7, 34, 78, 23]
SHUFFLE(my_list)

# constants.py
from constants import PI, GRAVITATIONAL_CONSTANT as grav, SPEED_OF_LIGHT as sped

radius = 5
area = PI * (radius ** 2)
print(f"Радиус круга: {radius}")
print(f"Площадь круга: {area:.2f}")

mass_kg = 1.2
energy = mass_kg * (sped ** 2)
print(f"Масса объекта: {mass_kg} кг")
print(f"Энергия объекта: {energy:.2e} ")

m1 = 1000
m2 = 500
r = 10
force = grav * ((m1 * m2) / (r ** 2))
print(f"Массы: {m1} кг и {m2} кг")
print(f"Расстояние: {r} м")
print(f"Сила гравитации: {force:.2e}")



