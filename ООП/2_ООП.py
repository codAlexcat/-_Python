# Задание 1
class Weapon:
    def __init__(self, damage, modifier):
        self.damage = damage
        self._modifier = modifier

    def __apply_modifier(self):
        return self.damage * self._modifier

    def get_final_damage(self):
        return self.__apply_modifier()

gun = Weapon(322, 1.5)
print(gun.get_final_damage())

# Задание 2
print("-" * 5, "Задание 2", "-" * 10)

class GameBank:
    def __init__(self):
        self._balance = 0

    def __log_transaction(self, operation, summa, status):
        s = None
        if status == True:
            s = "Успешно"
        else:
            s = "Ошибка!"

        if operation == "deposit":
            print(f"Операция: Пополнить баланс \n"
                  f"Сумма: {summa} \n"
                  f"Статус: {s}")
            print("_" * 100)
        elif operation == "withdraw":
            print(f"Операция: Снять \n"
                  f"Сумма: {summa} \n"
                  f"Статус: {s}")
            print("_" * 100)

    def deposit(self, summa):
        status = None
        old_balance = self._balance
        self._balance += summa

        if old_balance < self._balance:
            status = True
        else:
            status = False

        self.__log_transaction("deposit", summa, status)

    def withdraw(self, summa):
        status = None
        old_balance = self._balance

        if self._balance >= summa:
            self._balance -= summa
            if old_balance > self._balance:
                status = True
            else:
                status = False
        elif old_balance < self._balance:
            status = False

        self.__log_transaction("withdraw", summa, status)

    def show_balance(self):
        print(f"Ваш баланс: {self._balance}")
        print("_" * 100)

bank_Alex = GameBank()

bank_Alex.deposit(15000)

bank_Alex.withdraw(3000)
bank_Alex.show_balance()

bank_Alex.withdraw(100000)


