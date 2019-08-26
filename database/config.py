from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:postgres@localhost:5433/shopping_cart")
connect = engine.connect()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

from database import customer, product, wishlist, customer_cart
Base.metadata.create_all(bind=engine)


cus = customer.Customer()
pro = product.Product()
cus_cart = customer_cart.CustomerCart()
wish_list = wishlist.WishList()

# TODO: Check if any exception occur during database connectivity and handle it.
session.flush()
session.commit()
print("Database config successfully!")
session.close()
