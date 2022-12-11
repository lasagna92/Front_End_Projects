import sys


# ========The beginning of the class==========
class Shoe:
    """
    Class for an inventory program
    Attributes:
        country = str(origin country of the shoes)
        code = str(code of the shoes)
        products = str(name of the product)
        cost = int(cost of the product)
        quantity = int(stock quantity)
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.products = product
        self.cost = cost
        self.quantity = quantity
        """
        Parameters:
        country = str(origin country of the shoes)
        code = str(code of the shoes)
        products = str(name of the product) 
        cost = int(cost of the product)
        quantity = int(stock quantity)
           
        """

    def get_cost(self):
        """
        Method that return the cost of the product
        :return: self.cost
        """
        return self.cost

    def get_quantity(self):
        """
        Method that return the quantity of the product
        :return: self.quantity
        """
        return self.quantity

    def __str__(self):
        """
        Method that return the string representation of the class
        :return: self.country, self.code, self.products, self.cost, self.quantity
        """
        return f'{self.country} {self.code} {self.products} {self.cost} {self.quantity}'


# =============Shoe list===========
# List of class objects
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """
Function that read the data for a text file called inventory.txt
    """
    try:
        with open('inventory.txt', 'r') as f:  # Read the file inventory.txt
            # Loop through the lines of the file
            for line in f:
                # Skip the header
                if not line.startswith('Country'):
                    split_line = line.strip().split(',')
                    # Append every line as an object to the shoes_list
                    shoe_list.append(Shoe(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4]))

    except FileNotFoundError:
        print('\nFile not found!')
        sys.exit()


def capture_shoes():
    """
Allow the user to input a new product
    """
    country_input = str(input('\nPlease enter the country:\t'))
    code_input = input('Please enter the code:\t')
    product_input = str(input('Please enter the product:'))
    cost_input = int(input('Please enter the cost:\t'))
    quantity_input = int(input('Please enter the quantity:'))
    # Append the new created data to the object list
    shoe_list.append(Shoe(country_input, code_input, product_input, cost_input, quantity_input))
    # Append the data to the inventory.txt file
    with open('inventory.txt', 'a+') as f:
        f.write(f'\n{country_input},{code_input},{product_input},{cost_input},{quantity_input}')


def view_all():
    """
Display all the class object in the shoes_list as string
    """
    for obj in shoe_list:
        print(obj.__str__())


def re_stock():
    """
Re-stock the item with the lowest quantity
    """
    # Find the item with the lowest stock
    lowest_quantity = min(shoe_list, key=lambda shoe: int(shoe.get_quantity()))
    print(f'\n{lowest_quantity}')
    # Ask the user to enter the quantity to re-stock
    quantity = input('\nEnter quantity: ')
    # Update the list and the inventory.txt file
    lowest_quantity.quantity = quantity
    with open('inventory.txt', 'w') as f:
        for obj in shoe_list:
            f.write(f'{obj.country},{obj.code},{obj.products},{obj.cost},{obj.quantity}\n')


def search_shoe():
    """
Allow the user to search for shoes inputting their code and display the details
    """
    i = input('\nPlease enter the code:\t')
    for obj in shoe_list:
        code = obj.code
        if code == i:
            print(f'\n{obj.__str__()}')


def value_per_item():
    """
Calculate and display the value per item for each of the products
    """
    for obj in shoe_list:
        value = int(obj.get_cost()) * int(obj.get_quantity())
        print(f'The value of {obj.products} is: {value}')


def highest_qty():
    """
Find and print the product with the highest stock
    """
    highest_quantity = max(shoe_list, key=lambda shoe: int(shoe.get_quantity()))
    print(f'\n{highest_quantity}')


# ==========Main Menu=============

def main():
    """
Menu that allow the user to choose from different actions
    """
    while True:

        user_input = input('\nPlease choose one from the menu:\n'
                           '1. Read data\n'
                           '2. Add an item\n'
                           '3. View all the items\n'
                           '4. Re-stock\n'
                           '5. Search for a shoes\n'
                           '6. View value of items\n'
                           '7. View the product with the highest stock\n'
                           '8. Exit\n')

        if user_input == '1':
            # Call the read_shoes_data() function
            read_shoes_data()

        elif user_input == '2':
            # Call the capture_shoes() function
            capture_shoes()

        elif user_input == '3':
            # Call the view_all() function
            view_all()

        elif user_input == '4':
            # Call the re-stock() function
            re_stock()

        elif user_input == '5':
            # Call the search_shoes() function
            search_shoe()

        elif user_input == '6':
            # Call the value_per_item() function
            value_per_item()

        elif user_input == '7':
            # Call the highest_quantity() function
            highest_qty()

        elif user_input == '8':
            # Exit the program
            sys.exit()
        else:
            print('Incorrect input!')


main()
