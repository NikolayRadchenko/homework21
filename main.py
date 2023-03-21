from classes.request import Request
from classes.shop import Shop
from classes.store import Store

shop1 = Shop()
store1 = Store()
store1.add('собачки', 10)
store1.add('печеньки', 10)


def main(user_input):
    order_1 = Request(user_input)
    if order_1.product in store1.items:
        if store1.items[order_1.product] - order_1.amount >= 0:
            shop1.add(order_1.product, order_1.amount)
            store1.remove(order_1.product, order_1.amount)
            return f'Нужное количество есть на складе\n' \
                   f'Курьер забрал {order_1.amount} {order_1.product} со склада\n' \
                   f'Курьер везет {order_1.amount} {order_1.product} со склада в магазин\n' \
                   f'Курьер доставил {order_1.amount} {order_1.product} в магазин\n' \
                   f'\n' \
                   f'В складе хранится:\n' \
                   f'{store1.get_items()}\n' \
                   f'\n' \
                   f'В магазине хранится:\n' \
                   f'{shop1.get_items()}'
        else:
            return f'Такого количества товара нет в наличии'
    elif order_1.product not in store1.items and order_1.where_from in 'склада':
        return f'Данного товара нет на складе'
    elif order_1.product not in shop1.items and order_1.where_from in 'магазина':
        return f'Данного товара нет в магазине'



while True:
    order = input()

    print(main(order))
    user_input = input("Сделаете еще один заказ? Y/N\n")
    if user_input.upper() == 'Y':
        continue
    elif user_input.upper() == 'N':
        break
    else:
        print("Вы введи что-то не то")
        break
