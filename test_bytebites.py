from models import FoodItem, Menu, Receipt


# --- Test 1: The "Happy Path" ---
# Verify that a $10 burger and a $5 soda produce a total of $15.
def test_calculate_total_with_multiple_items():
    item1 = FoodItem("Spicy Burger", 10.0, "Burgers", 4.5)
    item2 = FoodItem("Large Soda", 5.0, "Drinks", 4.2)

    order = Receipt([item1, item2])

    assert order.calculate_total() == 15.0


# --- Test 2: The "Edge Case" ---
# Verify that an empty receipt produces a total of $0.
def test_order_total_is_zero_when_empty():
    order = Receipt([])

    assert order.calculate_total() == 0.0


# --- Test 3: The "Filtering Case" ---
# Verify that filtering for Drinks returns only drink items.
def test_filtering_menu_items_by_category():
    burger = FoodItem("Spicy Burger", 10.0, "Burgers", 4.5)
    soda = FoodItem("Large Soda", 5.0, "Drinks", 4.2)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)

    drink_results = menu.filter_by_category("Drinks")

    assert soda in drink_results
    assert burger not in drink_results