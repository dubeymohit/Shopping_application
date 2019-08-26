from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.config import Base


class WishList(Base):
    __tablename__ = 'wishlist'

    id = Column(Integer, autoincrement=True, primary_key=True)
    # user_id = relationship("Customer")
    # product_id = Column(Integer, ForeignKey("customer.id"))
