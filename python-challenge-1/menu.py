# Menu dictionary
menu_items = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza - Cheese": 8.99,
        "Pizza - Pepperoni": 10.99,
        "Pizza - Vegetarian": 9.99,    
        "Burger - Chicken": 7.49,
        "Burger - Beef": 8.49
        },
    "Drinks": {
        "Soda - Small": 1.99,
        "Soda - Medium": 2.49,
        "Soda - Large": 2.99,
        "Tea - Green": 2.49,
        "Tea - Thai iced": 3.99,
        "Tea - Irish breakfast": 2.49,
        "Coffee - Espresso": 2.99,
        "Coffee - Flat white": 2.99,
        "Coffee - Iced": 3.49
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake - New York": 4.99,
        "Cheesecake - Strawberry": 6.49,
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
Order = []
# [
#     {
#         "Item name": "string",
#         "Price": float,
#         "Quantity": int
#     },
#     {
#         "Item name": "string",
#         "Price": float,
#         "Quantity": int
#     },
# ]


# def print_menu():
#     print("Menu:")
#     for key, value in menu_items.items():
#         print(f"{key}. {value['Item name']} - ${value['Price']:.2f}")

# print_menu()

# #key value
# for key, value in menu_items.items():
#     print(key,value)
#     #print(f"{key}. {value['Item name']} - ${value['Price']:.2f}")


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_selection = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():
            # Save the menu category name to a variable
            menu_selection_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            print(f"You selected {menu_selection_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_selection_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_selectionname].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

menu_selection = input("Enter your selection from the menu: ")

# prompt customer to enter selection and validate input
while True:
    menu_selection = input("Enter your selection from the menu: ")
    if not menu_selection.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    
    menu_selection = int(menu_selection)
    if menu_selection not in menu_items:
        print("Selection not in menu. Please try again.")
        continue
    
    item_name = menu_items[menu_selection]["Item name"]
    price = menu_items[menu_selection]["Price"]
    
    quantity = input(f"Enter quantity for {item_name} (default 1): ")
    if not quantity.isdigit():
        quantity = 1
    else:
        quantity = int(quantity)
    
    order = {"Item name": item_name, "Price": price, "Quantity": quantity}
    order_list.append(order)
    
    continue_ordering = input("Would you like to continue ordering? (y/n): ").lower()
    if continue_ordering == "n":
        break
    elif continue_ordering != "y":
        print("Invalid input. Please try again.")

# Print order receipt
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    
    item_spaces = " " * (26 - len(item_name))
    price_spaces = " " * (6 - len(f"${price:.2f}"))
    
    print(f"{item_name}{item_spaces}| ${price:.2f}{price_spaces}| {quantity}")

total_price = sum(order["Price"] * order["Quantity"] for order in order_list)
print(f"Total: ${total_price:.2f}")





            # 2. Ask customer to input menu item number
            menu_selection = input("Type menu number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)


                # 4. Check if the menu selection is in the menu items
                if (menu_selection) in menu_items.keys():
                    # Store the item name as a variable
                    item_name = menu_items[menu_selection] ["item name"] 

                    # Ask the customer for the quantity of the menu item


                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list


                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

# loop through items in customer order

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    
    item_spaces = " " * (26 - len(item_name))
    price_spaces = " " * (6 - len(f"${price:.2f}"))
    
    print(f"{item_name}{item_spaces}| ${price:.2f}{price_spaces}| {quantity}")

# Calculate the total price
total_price = sum(order["Price"] * order["Quantity"] for order in order_list)
print("--------------------------|--------|----------")
print(f"Total                    |        | ${total_price:.2f}")


# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing


    # 9. Create space strings


    # 10. Print the item name, price, and quantity


# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
