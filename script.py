import json
import argparse

import os


def read_file():
    parser = argparse.ArgumentParser(description="Read a file and print its contents.")
    parser.add_argument("file", type=str, help="Name or path of the file to read")
    args = parser.parse_args()

# Open and read the file manually using a context manager
    try:
        with open(args.file, 'r', encoding='utf-8') as file:
            data = json.load(file) 
            ordered_items = []
            customers = []
            
            for order in data:
                customer = {
                  order.get("phone"): order.get("name"),
                }
                if customer not in customers:
                    customers.append(customer)
                else:
                    for existing in customers:
                        if list(existing.keys())[0] == list(customer.keys())[0]:
                            existing[list(existing.keys())[0]] = customer[list(customer.keys())[0]]

            if os.path.exists('customers.json'):        
                with open('customers.json', 'w') as final_file:
                      json.dump(customers, final_file, indent=4)
   
            else:
                with open('customers.json', 'w') as first_file:
                    json.dump(customers, first_file, indent=4)

            for items in data:
               

                food_ordered ={
                   items["items"][0].get("name"): {
                    "price": items["items"][0].get("price"),
                    "orders": 1

                    }
                }
                if food_ordered not in ordered_items:
                    ordered_items.append(food_ordered)
                else:
                    for item in ordered_items:
                        if list(item.keys())[0] == list(food_ordered.keys())[0]:
                            item[list(item.keys())[0]]["orders"] += 1

            if os.path.exists('items.json'):        
                with open('items.json', 'w') as items_file:
                      json.dump(ordered_items, items_file, indent=4)
   
            else:
                with open('items.json', 'w') as first_itemfile:
                    json.dump(ordered_items, first_itemfile, indent=4)



    except FileNotFoundError:
        print(f"Error: The file '{args.file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_file()

