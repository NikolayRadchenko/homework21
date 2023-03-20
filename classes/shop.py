from storage import Storage


class Shop(Storage):
    def __init__(self, capacity=20):
        super().__init__(capacity)

    def add(self, name, count):
        if self.get_free_space() - count >= 0 and len(self.get_items()) < 5:
            self.get_items()[name] = count
            self.capacity = self.get_free_space() - count

    def remove(self, name, count):
        if self.get_items()[name] >= count:
            self.get_items()[name] = self.get_items()[name] - count

    def get_free_space(self):
        return self.capacity

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)
