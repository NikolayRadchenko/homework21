from classes.request import Request
from classes.shop import Shop
from classes.store import Store


shop1 = Shop()
store1 = Store()


def main(user_input):
    order_1 = Request(user_input)
    print(order_1.__repr__())



