# Take shopping details and store then in database.

from database.product import Product
from database.customer import Customer


class CustomerActions:

    def __init__(self):
        pass

    @staticmethod
    def customer_action():
        """ Customer can perform the following task """
        print("\n------------------------------------------------------------------------------------")
        print("Select any one option: ")
        print(" 1. Browse all products. \n 2. Add Item to cart. \n 3. Add item to wise list. "
              "\n 4. Remove product from cart. \n 5. Remove product from wise list. \n 6. View order history "
              "\n 7. Exit.")
        choice = 0
        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Entered choice is invalid, Please select given options")

        if choice == 1:
            CustomerActions.browse_product()
        elif choice == 2:
            CustomerActions.add_product_to_cart()
        elif choice == 3:
            CustomerActions.add_product_to_wish_list()
        elif choice == 4:
            CustomerActions.remove_product_from_cart()
        elif choice == 5:
            CustomerActions.remove_product_from_wish_list()
        elif choice == 6:
            CustomerActions.view_order_history()
        elif choice == 7:
            exit()
        else:
            print("Your selected choice is wrong, please select again! :)")
            CustomerActions.customer_action()

    @staticmethod
    def browse_product():
        Product.browse_product()
        CustomerActions.customer_action()

    @staticmethod
    def add_product_to_cart():
        """ Add new product to the customer cart """
        print("Work is in progress")
        CustomerActions.customer_action()

    @staticmethod
    def remove_product_from_cart():
        """ Remove product from customer cart """
        print("Work is in progress")
        CustomerActions.customer_action()

    @staticmethod
    def add_product_to_wish_list():
        """ Add new product to the customer wish list """
        print("Work is in progress")
        CustomerActions.customer_action()

    @staticmethod
    def remove_product_from_wish_list():
        """ Remove product from customer wise list"""
        print("Work is in progress")
        CustomerActions.customer_action()

    @staticmethod
    def view_order_history():
        """ View order history of customer """
        print("Work is in progress")
        CustomerActions.customer_action()

    @staticmethod
    def delete_account():
        """ Only Customer can his/her delete """
        from shopping_cart.user import User
        print("Are you sure to delete your account.")
        response = input("Enter OK to delete account or CANCEL to don't delete.")
        if response.lower() == 'ok':
            Customer.delete_customer(User().email)

    @staticmethod
    def edit_account():
        """ Customer can edit account information """
        pass
