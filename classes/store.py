from storage import Storage


class Store(Storage):
    def __init__(self, capacity=100):
        super().__init__(capacity)

    def add(self, name, count):
        if self.get_free_space() - count >= 0:
            self.get_items()[name] = count
            self.capacity = self.get_free_space() - count
            return f"Нужное количество есть на складе\n" \
                   f"Курьер забрал {count} печеньки со склада\n" \
                   f"Курьер везет {count} печеньки со склада в магазин\n" \
                   f"Курьер доставил {count} печеньки в магазин\n" \
                   f"В складе хранится: {self.get_items()}"

    def remove(self, name, count):
        if self.get_items()[name] >= count:
            self.get_items()[name] = self.get_items()[name] - count

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)
