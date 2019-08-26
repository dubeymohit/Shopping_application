from sqlalchemy import (
        Column,
        Integer,
        String,
        Numeric,
    )
# from sqlalchemy.orm import relationship
# from database.product_list import Product
from database.config import Base, session as db_session


class Customer(Base):

    __tablename__ = "customer"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    email_id = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    mobile_number = Column(Numeric(10), nullable=False, unique=True)

    def __init__(self):
        pass

    def add_customer(self, name, email_id, password, mobile_number):
        self.name = name
        self.email_id = email_id
        self.password = password
        self.mobile_number = mobile_number

    @staticmethod
    def delete_customer(email_id):
        db_session.query(Customer).filter(Customer.email_id == email_id).delete()
        db_session.commit()
        db_session.close()
        print("Customer deleted successfully. :)")

    def add_product_to_cart(self):
        pass

    def remove_product_from_cart(self):
        pass

    def add_product_to_wise_list(self):
        pass

    def remove_product_from_wise_list(self):
        pass
