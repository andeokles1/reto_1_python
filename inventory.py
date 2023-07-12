#Python Advanced Course - Challenge #1
import pandas as pd


inventory = []

def add_product():
    global id
    name = input("Enter product's name: ")
    quantity = int(input("Enter product's quantity: "))
    price = float(input("Enter product's price: "))

    product = {'id': id,'name': name, 'quantity': quantity, 'price': price}
    print('The following product is about to be added into the inventory:')
    print(product)
    option = input('\nWould you like to add it? Y/N \n')
    if (option == 'Y' or option == 'y'):
        id += 1
        inventory.append(product)
        print('The product has been added to the inventory')
    else:
        option2 = input('\nWould you like to input again the product? Y/N \n')
        if (option2 == 'Y' or option == 'y'):
            add_product()
        else:
            return


def update_product():
    option_to_print = input('Would you like to see the inventory, so you can get the ID to update? (Y/N) \n')
    if (option_to_print == 'Y' or option_to_print == 'y'):
        print_inventory()
    id = int(input('\nPlease enter the id of the product you would like to update: '))
    for i in range(len(inventory)):
        if inventory[i]['id'] == id:
            while True:
                option = int(input('What would you like to update: \n 1- Name \n 2- Quantity \n 3- Price \n 4- Return to Main Menu \n'))
                if option == 1:
                    name = str(input('Enter the new name of the product: \n'))
                    inventory[i]['name'] = name
                if option == 2:
                    quantity = int(input('Enter the new quantity of the product: \n'))
                    inventory[i]['quantity'] = quantity
                if option == 3:
                    price = float(input('Enter the new quantity of the product: \n'))
                    inventory[i]['price'] = price
                if option == 4:
                    print('Returning to Main Menu \n')
                    return


def search_product():
    while True:
        option = int(input('Search by: \n 1- ID \n 2- Name \n 3- Quantity \n 4- Price \n 5- Exit \n'))
        if option == 1:
            id = int(input ('Enter ID to search: \n'))
            filtered_products = list(filter(lambda product: product['id'] == id, inventory))
        if option == 2:
            name = str(input ('Enter Name to search: \n'))
            filtered_products = list(filter(lambda product: product['name'].lower() == name.lower(), inventory))
        if option == 3:
            quantity = int(input ('Enter Quantity to search: \n'))
            filtered_products = list(filter(lambda product: product['quantity'] == quantity, inventory))
        if option == 4:
            price = int(input ('Enter Price to search: \n'))
            filtered_products = list(filter(lambda product: product['price'] == price, inventory))
        if option == 5:
            print('Returning to Main Menu \n')
            return

        if len(filtered_products) > 0:
            for product in filtered_products:
                print (product)
        else:
            print('No Products found')

def sortInventory():
    print('\n Which criteria would you like to sort by?\n')
    sortCriteria = Sorting_Selection()
    direction = int(input(f'''Would you like it 
      1. descending 
      2. ascending \n'''))
    sortProducts(sortCriteria, direction)
    print(inventory)


def sortProducts(sortCriteria, direction):
    inventory.sort(key=lambda product: product[sortCriteria], reverse=direction == 1)


def Sorting_Selection():
    keys = []
    count = 1
    for key in inventory[0].keys():
        print(f"{count}. {key}")
        count += 1
        keys.append(key)
    selectedField = int(input("Enter your choice: "))
    return keys[selectedField - 1]


def generate_inventory_report_csv():
    if len(inventory) > 0:
        df = pd.DataFrame(data=inventory)
        df.to_excel("inventory.xlsx", index=False)
        print("Inventory converted into excel...")
    else:
        print('Inventory is empty, not able to export')
        return


def delete_product():
    option_to_print = input('Would you like to see the inventory, so you can get the ID to delete it? (Y/N) \n')
    if (option_to_print == 'Y' or option_to_print == 'y'):
        print(inventory)
    id = int(input('\nPlease enter the id of the product you would like to delete it: '))
    for i in range(len(inventory)):
        if inventory[i]['id'] == id:
            product_deleted = inventory[i]
            del inventory[i]
            print(f'The product with ID: {product_deleted["id"]}, Name: {product_deleted["name"]}, Quantity: {product_deleted["quantity"]}, Price: {product_deleted["price"]} has been deleted')
            break

def print_inventory():
    if len(inventory) > 0:
        for product in inventory:
            print(f'ID: {product["id"]}, Name: {product["name"]}, Quantity: {product["quantity"]}, Price: {product["price"]}')
    else:
        print('Inventory is empty')
        return


def generate_month_annual_cost():
    monthly_cost = 0
    for product in inventory:
        monthly_cost = monthly_cost + (product['quantity']*product['price'])
    print(f'Monthly value of the inventory is: ${monthly_cost}')
    print(f'Annual value of the inventory is: ${monthly_cost*12}')



def inventory_menu():
    global id
    id = 1
    while True:
        print('')
        print('**************************Python Inventory*********************\n')
        print('1-. Add Product')
        print('2-. Update Product')
        print('3-. Search Product')
        print('4-. Sort Inventory by Name/Price/Quantity')
        print('5-. Delete Product')
        print('6-. Print Inventory')
        print('7-. Generate Inventory Report into an Excel File')
        print('8-. Generate Monthly/Annual Value Inventory')
        print('9-. Exit \n')

        choice = int(input('Please enter an option: '))
        if (choice == 1):
            add_product()
        if (choice == 2):
            update_product()
        if (choice == 3):
            search_product()
        if (choice == 4):
            sortInventory()
        if (choice == 5):
            delete_product()
        if (choice == 6):
            print_inventory()
        if (choice == 7):
            generate_inventory_report_csv()
        if (choice == 8):
            generate_month_annual_cost()
        if (choice == 9):
            print("Exiting...")
            break
inventory_menu()
