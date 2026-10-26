# ByteBites uses four classes: Customer tracks purchases, FoodItem stores food details,
# Menu manages food items, and Receipt groups items and calculates the total cost.


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, receipt):
        pass

    def view_purchase_history(self):
        pass


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        pass

    def filter_by_category(self, category):
        pass


class Receipt:
    def __init__(self, items):
        self.items = items
        self.total_cost = 0.0

    def calculate_total(self):
        pass