#Krishna Karthik Nanduri
#U21808967
#A Python class named "RetailItem" is defined in this program to represent an item in a retail store.
#The type of item, its quantity, and its price are all represented via properties in the class.



class RetailItem:
    def __init__(self, item_type, inventory_amount, item_price):
        self.__item_type = item_type
        self.__inventory_amount = inventory_amount
        self.__item_price = item_price
    
    def __str__(self):
        return f"{self.__item_type.ljust(15)} {str(self.__inventory_amount).rjust(15)} {str(self.__item_price).rjust(15)}"


def get_valid_input(prompt, input_type):
    while True:
        user_input = input(prompt)
        try:
            return input_type(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid value.")


def main():
    num_items = get_valid_input("How many items will you add today? ", int)
    while num_items < 1:
        print("Please enter a number of items greater than 0.")
        num_items = get_valid_input("How many items will you add today? ", int)
    
    items_list = []

    for i in range(1, num_items+1):
        item_type = input(f"Name of item {i}: ")
        inventory_amount = get_valid_input(f"Amount of item {i}: ", int)
        item_price = get_valid_input(f"Price of item {i}: $", float)
        item = RetailItem(item_type, inventory_amount, item_price)
        items_list.append(item)
    
    print("Here is a summary of the items you added:")
    print("\n{:<15} {:>15} {:>10}".format("Item", "Amount", "Price"))
    print("-" * 50)
    for item in items_list:
        print(item)

if __name__ == "__main__":
    main()
