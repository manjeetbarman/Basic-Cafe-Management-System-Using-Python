menu = {
    'pizza':149,
    'Allo Paratha':70,
    'Coffee': 60,
    'Momo': 80,
    'Veg Biriyani': 110,
}

print("Welcome to my cafe by Manjeet Barman")

print("Pizza: Rs149\nAllo Paratha: Rs70\nCoffee: Rs60\nMomo: Rs80\nVeg Biriyani: Rs110\n")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered Item {item_1} is not available right now! ")


another_order = input("Do you want to add another item ? (Yes/No)")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")

    else:
        print(f"Ordered Item {item_2} is not available right now! ")

print(f"The total amount of items to pay is {order_total}")

