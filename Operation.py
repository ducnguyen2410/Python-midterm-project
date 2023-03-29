import json
import os
class Operation:
    def __init__(self):
        self.control = {}

    def create(self):
        if os.path.getsize("/home/kali/Documents/code/projectg3/db.json") > 0:
            with open("/home/kali/Documents/code/projectg3/db.json", "r") as control:
                self.control = json.load(control)
        with open("/home/kali/Documents/code/projectg3/create.json", "r") as f:
            new_data = json.load(f)
        for i in new_data:
            for j in new_data[i]:
                category_id = i
                id = j
                name = new_data[i][id]["name"]
                price = new_data[i][id]["price"]
                stock = new_data[i][id]["stock"]
                description = new_data[i][id]["description"]
        if int(category_id) <= 0 or int(category_id) > 9:
            print("Category is not found. Please try again.")
        elif int(price) <= 0:
            print("Product price is not valid. Please try again.")
        elif int(stock) < 0:
            print("Product quantity is not valid. Please try again.")
        elif int(id) < 0:
            print("Product ID is invalid. Please try again.")
        elif len(description) == 0:
            print("You must add description for the product.")
        else:
            if category_id in self.control:
                if id in self.control[category_id]:
                    print("Product already exists.")
                    return
            else:
                self.control[category_id] = {}
            self.control[category_id][id] = {}
            self.control[category_id][id]["name"] = name
            self.control[category_id][id]["price"] = price
            self.control[category_id][id]["stock"] = stock
            self.control[category_id][id]["description"] = description
            with open("/home/kali/Documents/code/projectg3/db.json", "w") as out_file:
                json.dump(self.control, out_file)

    def update(self):
        if os.path.getsize("/home/kali/Documents/code/projectg3/db.json") > 0:
            with open("/home/kali/Documents/code/projectg3/db.json", "r") as control:
                self.control = json.load(control)
            with open("/home/kali/Documents/code/projectg3/update.json", "r") as read_file:
                data = json.load(read_file)
            for i in data:
                for j in data[i]:
                    category_id = i
                    id = j
                    name = data[i][id]["name"]
                    price = data[i][id]["price"]
                    stock = data[i][id]["stock"]
                    description = data[i][id]["description"]
            if int(category_id) <= 0 or int(category_id) > 9:
                print("Category is not found. Please try again.")
            elif category_id not in self.control:
                print(self.control)
                print("Could not find the specified product. Please try again.")
            elif id not in self.control[category_id]:
                print("ID of the product not found.")
            elif int(price) <= 0:
                print("Product price is not valid. Please try again.")
            elif int(stock) < 0:
                print("Product quantity is not valid. Please try again.")
            elif len(description) == 0:
                print("You must add description for the product.")
            else:
                self.control[category_id][id]["name"] = name
                self.control[category_id][id]["price"] = price
                self.control[category_id][id]["stock"] = stock
                self.control[category_id][id]["description"] = description
                with open("/home/kali/Documents/code/projectg3/db.json", "w") as out_file:
                    json.dump(self.control, out_file)
        else:
            print("Cannot update because the database is clear. Please add product.")

        



        
        

