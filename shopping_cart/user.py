# Take the credentials from user and check he/she is authorized or not.
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound

from database.config import session
from database.customer import Customer
from shopping_cart.admin import AdminActions
from shopping_cart.customer import CustomerActions
from shopping_cart.validate import validate_password, validate_email


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
        # Validate Email id
        while True:
            if not validate_email(email_id):
                print("Entered Email id is invalid. Please enter valid email id")
                email_id = input("Enter email id: ")
            else:
                try:
                    email_id_object = session.query(Customer).filter(Customer.email_id == email_id).one()
                    if email_id_object:
                        print("Email id already exist.")
                        email_id = input("Enter email id: ")

                except NoResultFound:
                    break

        # TODO: Use getpass module to take hidden password
        password = input("Enter password: ")
        # Validate Password
        while True:
            validate_pw = validate_password(password)
            if validate_pw[0]:
                print(validate_pw[1])
                break
            else:
                print(validate_pw[1])
                password = input("Enter password: ")

        confirm_password = input("Enter confirm password: ")
        while not password == confirm_password:
            print("Password and confirm password is not same. Please try again")
            password = input("Enter password: ")
            confirm_password = input("Enter confirm password: ")

        mobile_number = input("Enter your mobile number: ")
        # Validate mobile number
        while True:
            if not len(mobile_number) == 10:
                print("Entered mobile number is invalid. Please enter 10 digits mobile number")
                mobile_number = input("Enter mobile number: ")
            else:
                try:
                    mobile_no_object = session.query(Customer).filter(Customer.mobile_number == mobile_number).one()
                    if mobile_no_object:
                        print("Mobile number already exist")
                        mobile_number = input("Enter your mobile number: ")
                except NoResultFound:
                    break

        c = Customer()
        c.add_customer(name, email_id, password, mobile_number)
        session.add(c)
        session.commit()
        session.close()
