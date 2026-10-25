# Final ByteBites UML Class Diagram

```mermaid
classDiagram
    class Customer {
        +name: str
        +purchase_history: list~Receipt~
        +add_purchase(receipt: Receipt)
        +view_purchase_history() list~Receipt~
    }

    class FoodItem {
        +name: str
        +price: float
        +category: str
        +popularity_rating: float
    }

    class Menu {
        +items: list~FoodItem~
        +add_item(item: FoodItem)
        +filter_by_category(category: str) list~FoodItem~
    }

    class Receipt {
        +items: list~FoodItem~
        +total_cost: float
        +calculate_total() float
    }

    Menu "1" --> "0..*" FoodItem : lists
    Customer "1" --> "0..*" Receipt : records
    Receipt "1" --> "1..*" FoodItem : includes
```

## Relationship Summary

- A **Menu** lists zero or more **FoodItem** objects and can filter them by category.
- A **Customer** is managed by their `name` and keeps a `purchase_history` containing their past **Receipt** objects.
- A **Customer** can add a completed receipt to their purchase history and view that history.
- Each **Receipt** represents one single transaction and includes one or more selected **FoodItem** objects.
- A **Receipt** calculates the total cost from its selected items and stores the result in `total_cost`.
- The relationships to **FoodItem** are associations rather than compositions because menu items can be listed by the menu and included in receipts without either object owning the item's lifecycle.

## Why Mermaid?

Mermaid was used because it supports UML-style class-diagram notation and can render directly in Markdown previews, including VS Code. The diagram still uses standard class-diagram concepts such as classes, attributes, methods, associations, and multiplicities. It is not intended to represent a programming-language implementation.
