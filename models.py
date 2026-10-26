# ByteBites uses four classes: Customer tracks purchases, FoodItem stores food details,
# Menu manages food items, and Receipt groups items and calculates the total cost.


# Represents a customer and their purchase history.
class Customer:
    # Create a customer with an empty purchase history.
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    # Add a receipt to the customer's purchase history.
    def add_purchase(self, receipt):
        self.purchase_history.append(receipt)

    # Return the customer's past receipts.
    def view_purchase_history(self):
        return self.purchase_history


# Represents one food item sold by ByteBites.
class FoodItem:
    # Create a food item with its details.
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


# Manages the food items available on the menu.
class Menu:
    # Create an empty menu.
    def __init__(self):
        self.items = []

    # Add a food item to the menu.
    def add_item(self, item):
        self.items.append(item)

    # Return menu items that match a category.
    def filter_by_category(self, category):
        return [
            item for item in self.items
            if item.category.lower() == category.lower()
        ]

    # Return menu items sorted by price.
    def sort_by_price(self, ascending=True):
        return sorted(self.items, key=lambda item: item.price, reverse=not ascending)

    # Return menu items sorted by popularity.
    def sort_by_popularity(self, ascending=True):
        return sorted(
            self.items,
            key=lambda item: item.popularity_rating,
            reverse=not ascending,
        )

    # Return menu items sorted by name.
    def sort_by_name(self, ascending=True):
        return sorted(
            self.items,
            key=lambda item: item.name.lower(),
            reverse=not ascending,
        )


# Represents one customer transaction.
class Receipt:
    # Create a receipt containing selected food items.
    def __init__(self, items):
        self.items = items
        self.total_cost = 0.0

    # Calculate and return the total price of the receipt.
    def calculate_total(self):
        self.total_cost = sum(item.price for item in self.items)
        return self.total_cost


if __name__ == "__main__":
    menu = Menu()
    menu.add_item(FoodItem("Spicy Burger", 8.50, "Meals", 4.8))
    menu.add_item(FoodItem("Large Soda", 2.50, "Drinks", 4.1))
    menu.add_item(FoodItem("Apple Pie", 4.00, "Desserts", 4.6))

    print("Items in the Drinks category:")
    for item in menu.filter_by_category("Drinks"):
        print(f"- {item.name}: ${item.price:.2f}")

    print("\nMenu sorted by price:")
    for item in menu.sort_by_price():
        print(f"- {item.name}: ${item.price:.2f}")

    order = Receipt([menu.items[0], menu.items[1]])
    print(f"\nOrder total: ${order.calculate_total():.2f}")