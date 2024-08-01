# to manage and store the data on the database [ mysql, mongodb, plsql, postsql]

# methods
# create
# view 
# update
#delete

# implementing the menu system or funtion

def  create_item(idno, item, quantity, price):
    with open("inventory.txt", "a") as file:
        file.write(f"{idno},{item},{quantity},{price}\n")

def view_item():
    with open("inventory.txt", "r") as file:
        for line in file:
            print(line.strip())

def  update_item(idno, item, quantity):
    print(idno, item, quantity) # debug
    lines = []
    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    with open("inventory.txt", "w") as file:
        for line in lines:
            if line.startswith(idno):
                 X = line.strip().split(",")
                 file.write(f"{X[0]},{item}, {quantity}, {X[3]}\n")
            else:
                file.write(line)


def delete_item(idno):
    lines = []
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
    

    with open("inventory.txt", "w") as file:
        for line in lines:
            if not line.startswith(idno):
                file.write(line)


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
            create_item(idno, item, quantity, price)
        elif choice == "2":
            view_item()
        elif choice == "3":
            idno = input("enter the id: ")
            item = input("enterto update the name: ")
            quantity = int(input("enter item to update the quantity: "))
            # price = float(input("enter the price to update: "))
            update_item(idno, item, quantity)
        elif choice == "4":
            idno = input("enter the id: ")
            # item = input("enter item to delete: ")
            delete_item(idno)
        elif choice == "5":
            print("Exiting the menu system")
            break
        else: 
            print("invalid choice, pls try again")

#call the main  funtion
# if __name__ == "__main__":
main()
        