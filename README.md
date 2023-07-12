<h1>Challenge #1 - Advanced Python Class</h1>
Inventory Manager

Description of this program: The company you work for receives a large amount of raw materials and other products in its inventory, which are recorded and managed on sheets of paper that describe names, quantities, prices, types and sizes of each incoming and outgoing product. Recently some sheets were lost and the decision was made to digitize this process. Given this, you are asked to develop a program in Python, in which the person in charge of recording incoming and outgoing inventories, through the terminal of the operating system, can easily make these records.
The task should be carried out using functions to add new items, update quantities and search for specific items based on various criteria. Lambda functions should be used to sort the inventory based on different attributes, such as sorting items by name, quantity or price. In addition, nested functions should be used to handle complex operations, such as generating inventory reports or calculating the total value of the inventory.
This Python file should be uploaded to a Github repository, along with a README.md file explaining how to use the program.
The use of functions and lambda functions to add (with different data including date with the datetime package), edit, read, and delete products from the inventory will be evaluated, that everything works correctly and that contains the README file.
+ 3 more functions

+ Prerequisites
- Have Panda and openpyxl for excel exporting (pip install panda) and (pip install openpyxl)
- Python 3.9

Usage

Start the program by running the file inventory.py

Once you start the program, the following menu will appear

****************************Python Inventory***********************

1-. Add Product
2-. Update Product
3-. Search Product
4-. Sort Inventory by Name/Price/Quantity
5-. Delete Product
6-. Print Inventory
7-. Generate Inventory Report into an Excel File
8-. Generate Monthly/Annual Value Inventory
9-. Exit 

Find below the description of each of them:

1-. Add Product: It adds to the inventory a specific product (Name, Quantity and Price). It is saved in a list of dictionaries
Example:
Please enter an option: 1
Enter product's name: Plumas
Enter product's quantity: 50
Enter product's price: 9
The following product is about to be added into the inventory:
{'id': 1, 'name': 'Plumas', 'quantity': 50, 'price': 9.0}

Would you like to add it? Y/N 
y
The product has been added to the inventory

2-. Update Product:

Based on an ID of a product, the name/quantity/price is updated

Example:

Please enter an option: 2
Would you like to see the inventory, so you can get the ID to update? (Y/N) 
y
ID: 1, Name: Plumas, Quantity: 50, Price: 9.0

Please enter the id of the product you would like to update: 1
What would you like to update: 
 1- Name 
 2- Quantity 
 3- Price 
 4- Return to Main Menu 
1
Enter the new name of the product: 
Pluma
What would you like to update: 
 1- Name 
 2- Quantity 
 3- Price 
 4- Return to Main Menu 
2
Enter the new quantity of the product: 
40
What would you like to update: 
 1- Name 
 2- Quantity 
 3- Price 
 4- Return to Main Menu 
3
Enter the new quantity of the product: 
8
What would you like to update: 
 1- Name 
 2- Quantity 
 3- Price 
 4- Return to Main Menu 
4
Returning to Main Menu 


**************************Python Inventory*********************

1-. Add Product
2-. Update Product
3-. Search Product
4-. Sort Inventory by Name/Price/Quantity
5-. Delete Product
6-. Print Inventory
7-. Generate Inventory Report into an Excel File
8-. Generate Monthly/Annual Value Inventory
9-. Exit 

Please enter an option: 6
ID: 1, Name: Pluma, Quantity: 40, Price: 8.0

3-. Search Product: 
It searches a product by ID/Name/Quantity/Price

Example:

Please enter an option: 3
Search by: 
 1- ID 
 2- Name 
 3- Quantity 
 4- Price 
 5- Exit 
1
Enter ID to search: 
1
{'id': 1, 'name': 'Pluma', 'quantity': 40, 'price': 8.0}
Search by: 
 1- ID 
 2- Name 
 3- Quantity 
 4- Price 
 5- Exit 
2
Enter Name to search: 
Pluma
{'id': 1, 'name': 'Pluma', 'quantity': 40, 'price': 8.0}
Search by: 
 1- ID 
 2- Name 
 3- Quantity 
 4- Price 
 5- Exit 
3
Enter Quantity to search: 
40
{'id': 1, 'name': 'Pluma', 'quantity': 40, 'price': 8.0}
Search by: 
 1- ID 
 2- Name 
 3- Quantity 
 4- Price 
 5- Exit 
4
Enter Price to search: 
8
{'id': 1, 'name': 'Pluma', 'quantity': 40, 'price': 8.0}
Search by: 
 1- ID 
 2- Name 
 3- Quantity 
 4- Price 
 5- Exit 
5
Returning to Main Menu 

4-. Sort Inventory by Name/Price/Quantity:

It filters the inventory based on it's name, price or quantity and tries to order them ascending/descending

Example:

Please enter an option: 4

 Which criteria would you like to sort by?

1. id
2. name
3. quantity
4. price
Enter your choice: 1
Would you like it 
      1. descendent 
      2. ascendent 
1
[{'id': 3, 'name': 'Marcador', 'quantity': 34, 'price': 30.0}, {'id': 1, 'name': 'Pluma', 'quantity': 40, 'price': 8.0}]

**************************Python Inventory*********************

1-. Add Product
2-. Update Product
3-. Search Product
4-. Sort Inventory by Name/Price/Quantity
5-. Delete Product
6-. Print Inventory
7-. Generate Inventory Report into an Excel File
8-. Generate Monthly/Annual Value Inventory
9-. Exit 

Please enter an option: 4

 Which criteria would you like to sort by?

1. id
2. name
3. quantity
4. price
Enter your choice: 1
Would you like it 
      1. descendent 
      2. ascendent 
2
[{'id': 1, 'name': 'Pluma', 'quantity': 40, 'price': 8.0}, {'id': 3, 'name': 'Marcador', 'quantity': 34, 'price': 30.0}]

5-. Delete Product: Using an id, the program is able to delete a product in the inventory.

Example: 

Please enter an option: 5
Would you like to see the inventory, so you can get the ID to delete it? (Y/N) 
y
[{'id': 1, 'name': 'Pluma', 'quantity': 40, 'price': 8.0}, {'id': 2, 'name': 'Corrector', 'quantity': 20, 'price': 50.0}]

Please enter the id of the product you would like to delete it: 2
The product with ID: 2, Name: Corrector, Quantity: 20, Price: 50.0 has been deleted

**************************Python Inventory*********************

1-. Add Product
2-. Update Product
3-. Search Product
4-. Sort Inventory by Name/Price/Quantity
5-. Delete Product
6-. Print Inventory
7-. Generate Inventory Report into an Excel File
8-. Generate Monthly/Annual Value Inventory
9-. Exit 

Please enter an option: 6
ID: 1, Name: Pluma, Quantity: 40, Price: 8.0

6-. Print Inventory 
Prints in the terminal the content of the inventory (the content of the dictionary)

Example:

ID: 1, Name: Pluma, Quantity: 40, Price: 8.0

7-. Generate Inventory Report into an Excel File 
It basically uses a panda function to convert the inventory (the dictionary we are using) into an .XLSX file. It is created in the folder where the script is executed.

8-. Generate Monthly/Annual Value Inventory: 
When selecting this option, it prints the following information based on the input (inventory given)
Example:
Monthly value of the inventory is: $320.0
Annual value of the inventory is: $3840.0

Monthly Cost = It gets the costs for the products. This is obtained by multiplying the price and the quantity of the products
Annual Cost = Monthly Value * 12

9-. Exit: Terminates the program
