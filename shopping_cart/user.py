# Take the credentials from user and check he/she is authorized or not.
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound

from database.config import session
from database.customer import Customer
from shopping_cart.admin import AdminActions
from shopping_cart.customer import CustomerActions
# from getpass import getpass


class User:
    """ User identities for authentication and authorization."""

    def __init__(self):
        self.email = input("Enter your email id: ")
        self.password = input("Enter your Password: ")

        if self.email == "dubeymohit1997@gmail.com" and self.password == "Mohit#24":
            print("Welcome Admin")
            AdminActions.admin_action()
        else:
            print("Welcome Customer")
            try:
                # Check customer account exist or not
                all_email_password = session.query(Customer).filter(and_(Customer.email_id == self.email,
                                                                         Customer.password == self.password)).one()
                if all_email_password:
                    CustomerActions.customer_action()
            except NoResultFound:
                print("Account is not available for this email id. Please create your account! :)")
                User.add_user()
                CustomerActions.customer_action()

    @staticmethod
    def add_user():
        """ Add new user/customer """
        name = input("Enter your name: ")
        email_id = input("Enter email id: ")
        try:
            email = session.query(Customer).filter(Customer.email_id == email_id).one()
        except NoResultFound:
            pass

            password = input("Enter password: ")
            # getpass("Enter password: ", )
            confirm_password = input("Enter confirm password: ")
            # getpass("Enter confirm Password: ")
            while not password == confirm_password:
                print("Password and confirm password is not same. Please try again")
                password = input("Enter password: ")
                confirm_password = input("Enter confirm password: ")
            mobile_number = input("Enter your mobile number: ")
        c = Customer()
        c.add_customer(name, email_id, password, mobile_number)
        session.add(c)
        session.commit()
        session.close()

    @staticmethod
    def edit_user(self):
        """ User can edit personal information"""
        pass
