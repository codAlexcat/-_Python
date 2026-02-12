class Animal:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.happy = 50

    def feed(self):
        self.happy = min(100, self.happy + 25)
        return self.price // 10

class Lion(Animal): pass
class Panda(Animal): pass

class Zoo:
    def __init__(self, cash):
        self.cash = cash
        self.animals = []

    def buy(self, species, name, cost):
        if self.cash >= cost:
            self.cash -= cost
            self.animals.append(species(name, cost))
            print(f"Куплен {name}. Остаток: {self.cash}")

    def feed_all(self):
        for a in self.animals:
            cost = a.feed()
            if self.cash >= cost:
                self.cash -= cost
                print(f"{a.name} сыт (Счастье: {a.happy}). Потрачено: {cost}")

my_zoo = Zoo(1000)
my_zoo.buy(Lion, "Кот", 500)
my_zoo.feed_all()
print(f"Баланс: {my_zoo.cash}")


