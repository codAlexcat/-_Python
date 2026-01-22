# Задание 3
class Country:

    def __init__(self, name_country, name_continent, people, phone_cod, name_capital, name_city):
        self.name_country = name_country
        self.name_continent = name_continent
        self.people = people
        self.phone_cod = phone_cod
        self.name_capital = name_capital
        self.name_city = name_city

    def show_info(self):
        print(f"Информация о стране: {self.name_country} \n"
              f"Название континента: {self.name_continent} \n"
              f"Численность населения: {self.people} \n"
              f"Телефонный код страны: {self.phone_cod} \n"
              f"Название столицы: {self.name_capital} \n"
              f"Название городов страны: {self.name_city}")


country1= Country("Россия", "Евразия", 146_447_424, "+7", "Москва", ...)
country1.name_city = ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]

country2 = Country("США", "Северная Америка", 331_900_000, "+1", "Вашингтон", ...)
country2.name_city = ["Нью-Йорк", "Лос-Анджелес", "Чикаго", "Хьюстон", "Финикс", "Финляндия"]

country2.show_info()
country1.show_info()

# Задание 4
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # Установка значений
    def set_numerator(self, value):
        self.numerator = value

    def set_denominator(self, value):
        if value != 0:
            self.denominator = value

    # Получение значений
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    # Вывод
    def show(self):
        print(f"{self.numerator}/{self.denominator}")

    def double(self):
        self.numerator *= 2

    def invert(self):
        self.numerator, self.denominator = self.denominator, self.numerator

    def simplify(self):
        if self.numerator % 2 == 0 and self.denominator % 2 == 0:
            self.numerator //= 2
            self.denominator //= 2

# Теперь работает
frac = Fraction(2, 10)
frac.show()

frac.double()
frac.show()

frac.simplify()
frac.show()

frac.invert()
frac.show()
