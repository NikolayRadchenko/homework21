class Request:
    def __init__(self, user_input):
        data = self.get_data(user_input)
        if len(data) == 7:
            self.where_from = data[4]
            self.to = data[6]
            self.amount = int(data[1])
            self.product = data[2]
        elif len(data) == 6:
            self.where_from = data[5]
            self.to = 'магазин'
            self.amount = int(data[2])
            self.product = data[3]

    def get_data(self, user_input):
        return user_input.split(" ")

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} из {self.where_from} в {self.to}'
