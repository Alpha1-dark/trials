# Contact Manager
# --------------------------
# Start with this phone directory:
# phone_directory = {
#     "John Smith": "555-0123",
#     "Mary Johnson": "555-4567",
#     "David Wilson": "555-8901"
# }
 
# Tasks:
# a) add a new contact, making sure you don't duplicate entries
# b) delete a contact
# c) update an existing contact's number
# d) find all contacts that start with a given letter
 
# Example output for part d) with letter "M":
# {"Mary Johnson": "555-4567"}

# SOLUTIONS.

# phone_directory = {
#     "John Smith": "555-0123",
#     "Mary Johnson": "555-4567",
#     "David Wilson": "555-8901"
# }
 
# #adding a new contact;S
# phone_directory['Bakunga Alpha'] = "555-2568"
# print()
# print(phone_directory)

# #deleting a contact;
# del phone_directory["David Wilson"]
# print()
# print(phone_directory)

# #updating an existing number;
# phone_directory.update({"Mary Johnson":"555-000"})
# print()
# print(phone_directory)
# print()

# #outputting contacts that start with "m";
# for names, contacts in phone_directory.items():
#     if names.startswith("M"):
#         print(f"{names} : {contacts}")
#         print()

        ##                                         END.




# Store Inventory Manager
# ---------------------------------
# You manage a small grocery store with this inventory:
# inventory = {
#     "apple": {"price": 0.50, "quantity": 100},
#     "banana": {"price": 0.75, "quantity": 150},
#     "orange": {"price": 0.60, "quantity": 75}
# }
 
# Tasks:
# a) Returns all products with quantity less than 80
# b) Calculate the total value of your inventory (price * quantity for each item)
# c) Update the price of bananas to $0.80
# has context menu.

# SOLUTIONS;

inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.75, "quantity": 150},
    "orange": {"price": 0.60, "quantity": 75}
}

#returning all produts  with quantity less than 80;
for fruits, dem_prices in inventory.items():
    if dem_prices["quantity"] < 80:
        print()
        print(f"{fruits} has the  quantity of less than 80. ")
        print()

#calculating the total value of the inventory (price * quantity for each item);
for items, prices in inventory.items():
    total = prices["price"] * prices["quantity"]
    print(f"{items} has a total value of ${total}.\n")  

#updating the price of bananas to $0.80;
inventory["banana"]["price"] = 0.800
print()
print(inventory)
print()