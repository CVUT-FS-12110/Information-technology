import json


# --- Load product catalog ---
def load_catalog():
    """
    [
        {"id": 1, "name": "Apples", "price": 2.5},
        {"id": 2, "name": "Bread", "price": 1.8},
        {"id": 3, "name": "Milk", "price": 1.2}
    ]
    """
    return json.loads(load_catalog.__doc__)


# --- Add item to cart ---
def add_item(cart, catalog):
    print("\nAvailable products:")
    for product in catalog:
        print(f"{product['id']}. {product['name']} - ${product['price']}")
    try:
        choice = int(input("Select product ID to add: "))
    except ValueError:
        print("Invalid input.\n")
        return cart

    # Add matching product
    return cart + [p for p in catalog if p["id"] == choice]


# --- Checkout ---
def checkout(cart):
    total = sum(item["price"] for item in cart)
    items = "\n".join(f"- {item['name']} ${item['price']}" for item in cart)
    return f"\nReceipt:\n{items}\nTotal: ${total:.2f}"


# --- Run pipeline ---
def run():
    catalog = load_catalog()
    cart = []

    while True:
        action = input("\nAdd item (a) or Checkout (c)? ").lower()
        if action == "a":
            cart = add_item(cart, catalog)
        elif action == "c":
            if not cart:
                print("Cart is empty! Cannot checkout.")
            else:
                print(checkout(cart))
                break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    run()
