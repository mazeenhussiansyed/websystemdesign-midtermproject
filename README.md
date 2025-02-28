# websystemdesign-midtermproject
Project Overview
We have a JSON file and two Python programs that take this JSON file as input and output useful information, such as client information (phone numbers and names), menu items, their prices, and the number of orders made.

customer.json: This is the output of the customer.py program.
items.json: This is the output of the items.py program.
Installation Instructions
1. Install Python version 3.3 or higher.
2. Install Git and GitHub account.
3. New repository should be created.
4. Needed libraries have to be imported.
Functionality and Design Implementation
customer.py
The customer.py script accepts data from the file example_orders.json. The script proceeds to the main method, which calls the read_object() function to open and return the JSON file. The function extract_customer_data() is then called to fetch the necessary customer information, which is stored in the customer_data() variable. The script creates a new file customer.json, containing the phone number and name of the customer.

items.py
The items.py script also takes example_orders.json as an input. The main function invokes read_orders() to read the input JSON file. It then invokes the process_items() function to extract the items listed in the file. The script checks if each item already exists in the items dictionary. If the item is not present, it is added to the dictionary with its price and the order count is made one. If the item is already there, its order number is incremented by one. Then the script writes a new items.json file that includes the item name, price of the item, and the number of orders received for the item.

File Structure
Ensure all the files are in the same directory.

Once the two Python scripts have been executed, the files customer.json and items.json will be available in the same directory.
