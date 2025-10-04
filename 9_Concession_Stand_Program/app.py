# Concession stand Program with Python

menu = {"pizza": 3.00,
        "nachos": 4.5,
        "popcorn": 6.00,
        "fries": 2.5,
        "chips": 1.00,
        "pretzel": 3.5,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("========== MENU ==========")
for k, v in menu.items():
    print(f"{k:15}: ${v:.2f}")
print("==========================")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)

print("========== YOUR ORDER ==========")
for f in cart:
    print(f, end=" ")
print()
print(f"Total is: ${total:.2f}")

