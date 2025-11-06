# Магазин предметов
# Задачка, магазин, просмотр, подсчет, покупка, инвентарь

shopItems = ["Зелье здоровья", "Зелье маны", "Меч", "Щит"] # какие есть предметы
prices = [50, 75, 200, 150] # цена предметов
stock = [10, 8, 3, 5] # количество этих предметов
wallet = 10000
quantity_inventory = [0, 0, 0, 0]
inventory_user = ["Зелье здоровья", "Зелье маны", "Меч", "Щит"]


# Функция номер 1. Показ товара магазина
def ShowShop(stock, prices, shopItems):
    print("Витрина магазина: ")
    if stock[0] > 0:
        print(f"{shopItems[0]}   | {prices[0]} кредитов  | {stock[0]} штук |")
    else:
        print(f"{shopItems[0]}   | {prices[0]} кредитов  | {stock[0]} штук | Товар закончился")

    if stock[1] > 0:
        print(f"{shopItems[1]}       | {prices[1]} кредитов  | {stock[1]} штук  |")
    else:
        print(f"{shopItems[1]}       | {prices[1]} кредитов  | {stock[1]} штук  | Товар закончился")

    if stock[2] > 0:
        print(f"{shopItems[2]}              | {prices[2]} кредитов | {stock[2]} штук  |")
    else:
        print(f"{shopItems[2]}              | {prices[2]} кредитов | {stock[2]} штук  | Товар закончился")

    if stock[3] > 0:
        print(f"{shopItems[3]}              | {prices[3]} кредитов | {stock[3]} штук  |")
    else:
        print(f"{shopItems[3]}              | {prices[3]} кредитов | {stock[3]} штук  | Товар закончился")


# Функция номер 2. Подсчет цены
def price_calculation():
    print("Подсчет цены:")
    print("Введите необходимое вам количество товара: ")
    product1 = int(input(f"'{shopItems[0]}', всего {stock[0]} штук: "))
    product2 = int(input(f"'{shopItems[1]}', всего {stock[1]} штук: "))
    product3 = int(input(f"'{shopItems[2]}', всего {stock[2]} штук: "))
    product4 = int(input(f"'{shopItems[3]}', всего {stock[3]} штук: "))

    prices1 = prices[0] * product1
    prices2 = prices[1] * product2
    prices3 = prices[2] * product3
    prices4 = prices[3] * product4
    prices_end = prices1 + prices2 + prices3 + prices4  # Итоговая сумма
    print(f"Итоговая сумма товаров: {prices_end} кредитов")

# Функция номер 3. Покупка товара
# def Buy_item(wallet, stock):
#     print(shopItems)
#     num = int(input("Товар с каким номером по счету вы хотите купить: ")) - 1
#     quantity = int(input(f"Введите количество товара, всего его {stock[num]} штук: "))
#     price = prices[num] * quantity
#     wallet -= price
#     stock[num] -= quantity
#     print(f"Спасибо за покупку! \nУ вас на счету осталось {wallet} кредитов")
#     quantity_inventory = [0, 0, 0, 0]
#     inventory_user = ["Зелье здоровья", "Зелье маны", "Меч", "Щит"]
#     quantity_inventory.insert(num, quantity)


# Функция номер 4. Показа инвентаря
def inventory(quantity_inventory, inventory_user, wallet):
    print("Ваш инвентарь: ")
    print(f"Ваш счет: {wallet} кредитов")
    print("_" * 100)
    if quantity_inventory[0] == 0 and quantity_inventory[1] == 0 and quantity_inventory[2] == 0 and quantity_inventory[3] == 0:
        print("У вас пока что нету предметов! ")
    else:
        if quantity_inventory[0] > 0:
            print(f"{inventory_user[0]} | {quantity_inventory[0]} шт ")

        if quantity_inventory[1] > 0:
            print(f"{inventory_user[1]}     | {quantity_inventory[1]} шт ")

        if quantity_inventory[2] > 0:
            print(f"{inventory_user[2]}            | {quantity_inventory[2]} шт ")

        if quantity_inventory[3] > 0:
            print(f"{inventory_user[3]}            | {quantity_inventory[3]} шт ")


while True:
    print("_" * 100)
    function = int(input("Выберите что вы хотите сделать: \n1 - Просмотр товара | 2 - Подсчет цены | 3 - Покупка товара | 4 - Просмотреть свой инвентарь: "))
    print("_" * 100)
    if function == 1:
        print("_" * 100)
        ShowShop(stock, prices, shopItems)

    elif function == 2:
        print("_" * 100)
        price_calculation()

    elif function == 3:
        print("_" * 100)
        print(shopItems)
        num = int(input("Товар с каким номером по счету вы хотите купить: ")) - 1
        if stock[num] == 0:
            print("К сожалению товар закончился! ")
        else:
            quantity = int(input(f"Введите количество товара, всего его {stock[num]} штук: "))
            price = prices[num] * quantity
            wallet -= price
            stock[num] -= quantity
            print(f"Спасибо за покупку! \nУ вас на счету осталось {wallet} кредитов")
            quantity_inventory = [0, 0, 0, 0]
            inventory_user = ["Зелье здоровья", "Зелье маны", "Меч", "Щит"]
            quantity_inventory.insert(num, quantity)

    elif function == 4:
        inventory(quantity_inventory, inventory_user, wallet)




