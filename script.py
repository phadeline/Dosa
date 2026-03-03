import json
import argparse
file_path = 'example_orders.json'
import os


def read_file(file):
    parser = argparse.ArgumentParser(description="Read a file and print its contents.")
    parser.add_argument("file", type=str, help="Name or path of the file to read")
    args = parser.parse_args()

# Open and read the file manually using a context manager
    try:
        with open(args.file, 'r', encoding='utf-8') as file:
            data = json.load(file) 
            ordered_items []
            customers = []
            
            for order in data:
                customer = {
                  order.get("phone"): order.get("name"),
                }
                customers.append(customer)
            if os.path.exists('customers.json'):        
                with open('customers.json', 'w') as final_file:
                      json.dump(customers, final_file, indent=4)
   
            else:
                with open('customers.json', 'w') as first_file:
                    json.dump(customers, first_file, indent=4)

            for items in data:
                food_ordered ={
                   items.get("names"): {
                    "price": items.get("price"),
                    "orders": 1
                    }
                }



    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_file(file_path)

