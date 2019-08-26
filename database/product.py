from sqlalchemy import (
        Column,
        Integer,
        String,
    )
from database.config import Base, connect, session as db_session
from pandas import read_sql


class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(32), nullable=False)
    price = Column(Integer, nullable=False)
    available_quantity = Column(Integer, nullable=False)

    def add_product(self, name, price, available_quantity):
        self.name = name
        self.price = price
        self.available_quantity = available_quantity

    @staticmethod
    def delete_product():
        print("Available products are following: ")
        Product.browse_product()
        p_id = input("\nEnter the product id which you what to delete: ")
        db_session.query(Product).filter(Product.id == p_id).delete()
        db_session.commit()
        db_session.close()

    @staticmethod
    def browse_product():
        df = read_sql("SELECT * from product", connect)
        if df.empty:
            print("Products are not available now")
        else:
            print(df)
        db_session.close()
