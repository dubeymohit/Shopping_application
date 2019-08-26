# Take shopping details and store then in database.

from database.config import connect, session as db_session
from database.product import Product
from pandas import read_sql


class AdminActions:

    @staticmethod
    def admin_action():
        """ Admin can perform the following task """
        print("\n------------------------------------------------------------------------------------")
        print("Select any one option: ")
        print(" 1. Add new Product. \n 2. Delete any existing product. \n 3. Edit any existing item. "
              "\n 4. Browse all products. \n 5. Browse all customer account. \n 6. Exit.")
        choice = 0
        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Entered choice is invalid, Please select given options")

        if choice == 1:
            AdminActions.add_product()
        elif choice == 2:
            AdminActions.delete_product()
        elif choice == 3:
            AdminActions.edit_product()
        elif choice == 4:
            AdminActions.browse_product()
        elif choice == 5:
            AdminActions.browse_customer()
        elif choice == 6:
            exit()
        else:
            print("Your selected choice is wrong, please select again! :)")

    @staticmethod
    def add_product():
        """ Add new product """
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        available_quantity = input("Enter available quantity of product: ")
        p = Product()
        p.add_product(name, price, available_quantity)
        db_session.add(p)
        db_session.commit()
        db_session.close()
        print("New product added successfully! :) \n\n")
        AdminActions.admin_action()

    @staticmethod
    def delete_product():
        Product.delete_product()
        print("Product deleted successfully. :) \n\n")
        AdminActions.admin_action()

    @staticmethod
    def edit_product():
        pass

    @staticmethod
    def browse_product():
        Product.browse_product()
        AdminActions.admin_action()

    @staticmethod
    def browse_customer():
        df = read_sql("SELECT * from customer", connect)
        if df.empty:
            print("Customers are not available now")
            AdminActions.admin_action()
        else:
            print(df)
            AdminActions.admin_action()
        db_session.close()

