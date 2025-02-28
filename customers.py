import json

def read_orders(filename):
    """Reads orders from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

def extract_customer_data(orders):
    """Extracts customer phone numbers and names."""
    customer_data = {}
    for order in orders:
        phone = order.get("phone")
        name = order.get("name")
        if phone and name:
            customer_data[phone] = name  # Store phone number as key, name as value
    return customer_data

def main():
    """Processes customer data and writes to customers.json."""
    orders = read_orders('example_orders.json')
    customer_data = extract_customer_data(orders)
    
    with open('customers.json', 'w') as f:
        json.dump(customer_data, f, indent=2)

if __name__ == "__main__":
    main()