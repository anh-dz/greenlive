<<<<<<< HEAD
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from typing import List

class Base(DeclarativeBase):
    pass

class Links_point(Base):
    __tablename__ = "links_point"
    id:Mapped[int] = mapped_column(primary_key=True)
    address:Mapped[str] = mapped_column(nullable=False)
    start:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self): 
        return f"ID: {self.id} Address: {self.address} Start_time: {self.start}"

class Thong_ke(Base):
    __tablename__ = "thong_ke"
    id:Mapped[int] = mapped_column(primary_key=True)
    QR_created:Mapped[int] = mapped_column(nullable=False)
    QR_scanned:Mapped[int] = mapped_column(nullable=False)
    QR_active:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self):
        return f"ID: {self.id} QR created: {self.QR_created} QR scanned: {self.QR_scanned} QR active: {self.QR_active}"
    
class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str] = mapped_column(nullable=False)
    #user type là 1 hoặc 2; 1 là ng mua Buyer, 2 là ng bán Seller
    user_type:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self):
        return f"id: {id} username: {self.username} password: {self.password} user_type: {self.user_type}"
    
class Buyer(Base):
    __tablename__ = "buyers"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(nullable=False)
    point_gained:Mapped[int] = mapped_column(nullable=False)

class Seller(Base):
    __tablename__ = "sellers"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(nullable=False)
    qr_made:Mapped[int] = mapped_column(nullable=False)

class History_user(Base):
    __tablename__ = "history_user"
    id:Mapped[int] = mapped_column(primary_key=True)
    point_gained:Mapped[int] = mapped_column(nullable=False)
    time:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self) -> str:
        return f"id: {self.id} point_gained: {self.point_gained} time: {self.time} user_id: {self.user_id}"
=======
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from typing import List

class Base(DeclarativeBase):
    pass

class Links_point(Base):
    __tablename__ = "links_point"
    id:Mapped[int] = mapped_column(primary_key=True)
    address:Mapped[str] = mapped_column(nullable=False)
    start:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self): 
        return f"ID: {self.id} Address: {self.address} Start_time: {self.start}"

class Thong_ke(Base):
    __tablename__ = "thong_ke"
    id:Mapped[int] = mapped_column(primary_key=True)
    QR_created:Mapped[int] = mapped_column(nullable=False)
    QR_scanned:Mapped[int] = mapped_column(nullable=False)
    QR_active:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self):
        return f"ID: {self.id} QR created: {self.QR_created} QR scanned: {self.QR_scanned} QR active: {self.QR_active}"
    
class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str] = mapped_column(nullable=False)
    buyer:Mapped["Buyer"] = relationship(back_populates = "user")
    seller:Mapped["Seller"] = relationship(back_populates = "user")
    history:Mapped["History_user"] = relationship(back_populates="user")
    def __repr__(self):
        return f"id: {id} username: {self.username} password: {self.password}"
    
class Buyer(Base):
    __tablename__ = "buyers"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    point_gained:Mapped[int] = mapped_column(nullable=False)
    user:Mapped["User"] = relationship(back_populates = "buyer")

class Seller(Base):
    __tablename__ = "sellers"
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    qr_made:Mapped[int] = mapped_column(nullable=False)
    user:Mapped["User"] = relationship(back_populates = "seller")

class History_user(Base):
    __tablename__ = "history_user"
    id:Mapped[int] = mapped_column(primary_key=True)
    point_gained:Mapped[int] = mapped_column(nullable=False)
    time:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    user:Mapped["User"] = relationship(back_populates="history")
>>>>>>> 31214a3bc26fe888fd3acafeb5d466ee82a3a743
