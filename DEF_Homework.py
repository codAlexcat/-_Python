import random

while True:
    # Функция первая. Генерация пароля из определенных символов
    def password_generation(length):
        special = '!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        digits = "0123456789"
        password = ""

        while length < 4:
            print("в пароле должно быть не менее 4 символов! ")
            length = int(input("Введите длину пароля заново: "))

        password = [
            random.choice(special),
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits)
        ]
        general = special + uppercase + lowercase + digits

        if length > 4:
            for i in range(length - 4):
                password += random.choice(general)
        password = "".join(password)
        return password

    # вторая функция проверки надежности пароля
    def Reliability_check(password):
            max_count = 0
            for i in password:
                count = password.count(i) # проверяет сколько раз символ i встречается в строке
                if count > max_count:
                    max_count = count

            if max_count > 3:
                return "Слабый"
            elif max_count == 3:
                return "Средний"
            else:
                return "Хороший"

    # третья функция для проверки на повтор пароля
    def individual_password(my_password):
        used_passwords = []

        if my_password in used_passwords:
            print("Такой пароль уже был!")

        used_passwords.append(my_password)


    length = int(input("Введите длину пароля: "))
    my_password = password_generation(length)  # Сохраняем пароль

    print(f"Пароль: {my_password}")
    print(f"Надежность: {Reliability_check(my_password)}")

    individual_password(my_password)

    user = input("Хотите сгенерировать пароль (да/нет): ")
    if user == "нет":
        break

