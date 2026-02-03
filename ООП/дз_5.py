import math

class Vector2D:
    def __init__(self, x, y):
        # Атрибуты x и y
        self.x = x
        self.y = y
    # плюс
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    # минус
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    # длина вектора
    def length(self):
        return math.sqrt((self.x**2 + self.y**2))
    # преобразование в строку
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector2D(7, 3)
v2 = Vector2D(4, 11)

print(v1 - v2)
print(v1 + v2)
print(v2.length())
print(v1)
