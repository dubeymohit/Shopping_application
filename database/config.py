from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import relationship

engine = create_engine("postgresql://postgres:postgres@localhost:5433/shopping_cart")
connect = engine.connect()
Base = declarative_base()


# from database.customer import Customer
# from database.product_list import Product


"""
class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    email_id = Column(String, nullable=False)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(32))
    quantity = Column('quantity', Integer)
    price = Column('price', Numeric)


class WiseList(Base):
    __tablename__ = 'wiselist'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = relationship("Customer")
    product_id = Column(Integer, ForeignKey("customer.id"))


class UserCart(Base):
    __tablename__ = 'usercart'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = relationship("Customer")
    product_id = Column(Integer, ForeignKey("customer.id"))
"""
'''
class Config:
    """ Configure the relations """
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.flush()
        session.commit()
        print("Database config successfully!")
        session.close()
'''
Session = sessionmaker(bind=engine)
session = Session()

from database import customer, product, wishlist, customer_cart
Base.metadata.create_all(bind=engine)


cus = customer.Customer()
pro = product.Product()
cus_cart = customer_cart.CustomerCart()
wish_list = wishlist.WishList()

session.flush()
session.commit()
print("Database config successfully!")
session.close()

'''
if __name__ == "__main__":
    pass

    # Customer.id = 1
    # Customer.name = "Mohit"
    # Customer.email_id = "dubeymohit1997@gmil.com"
    # session.add(Customer)

    # Base.metadata.create_all(bind=engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # obj1 = customer.Customer()
    # obj2 = product_list.Product()
    # obj1.Bs.append(obj2)
    # session.add(obj1)
    # session.flush()
    # session.commit()
    # session.close(

from psycopg2 import connect


# Connect to the database
conn = connect(
            host="localhost",
            database="shopping_cart",
            port=5433,
            user="postgres",
            password="postgres",
        )

conn.close()
'''
