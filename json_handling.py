#full form of the JSon

import json 

# data = {
#     "name":"subbu",
#     "age":"30",
#     "city": "AP",
#     "is_student": false,
#     "scores": [85, 92, 78]
# }


# with open("data.json","w") as json_file:
#     json.dump(data, json_file)  # u can write data on file

# with  open("data.json", "r") as json_file:
#     X = json.load(json_file) #u can read the data on file

# print(X)


# json handling inventory mangement system


def create_item(idno, item, quantity, price):

    content = {
        "idno": idno,
        "item": item,
        "quantity": quantity,
        "price": price

    }

    with open ("inventory.json", "w") as file:
        json.dump(content, file, indent=4)


def view_item():
    with  open("inventory.json", "r") as json_file:
        X = json.load(json_file) #u can read the data on file
    print(X)



def update_item(idno, item_name, quantity, price):
    # print(item_name, quantity)
    try:
        with open('inventory.json', 'r') as file:
            content = json.load(file)
            # print(content)
    except FileExistsError:
        print("data is empty")
        return
    # print(content)
    # {'item': 'subbu', 'quantity': 20, 'price': 30.0}

    if content["idno"] == idno:
        content["item"] = item_name,
        content["quantity"] = quantity,
        content["price"] = price
   

    with open ("inventory.json", "w") as file:
        json.dump(content, file, indent=4)


def delete_item(idno):
    # print(item_name)
    try:
        with open('inventory.json', 'r') as file:
            content = json.load(file)
            print(content)
    except FileExistsError:
        print("data is empty")
        return
    # content = [item for item in content if item["item"] != item]
    if content["idno"] == idno:
        content={}
  

    with open ("inventory.json", "w") as file:
        json.dump(content, file, indent=4)



def main():
    while True:
        print("\nThis is Inventory Mangement system")
        print("1. Create item")
        print("2. View item")
        print("3. Update item")
        print("4. Delete item")
        print("5. Exit")

        # menu input value system
        choice = input("enter your menu:")
        
        # menu system
        if choice == "1":
            idno = input("enter the id: ")
            item = input("enter the name: ")
            quantity = int(input("enter the quantity: "))
            price = float(input("enter the price: "))
            create_item( idno, item, quantity, price)
        elif choice == "2":
            view_item()
        elif choice == "3":
            idno = input("enter the id: ")
            item_name = input("enterto update the name: ")
            quantity = int(input("enter item to update the quantity: "))
            price = float(input("enter the price to update: "))
            update_item( idno, item_name, quantity, price)
        elif choice == "4":
            idno = input("enter the id: ")
            # item_name = input("enter item to delete: ")
            delete_item(idno)
        elif choice == "5":
            print("Exiting the menu system")
            break
        else: 
            print("invalid choice, pls try again")

#call the main  funtion
# if __name__ == "__main__":
main()