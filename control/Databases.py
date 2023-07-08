from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin
class Base(DeclarativeBase):
    pass

class Links_point(Base):
    __tablename__ = "links_point"
    id:Mapped[int] = mapped_column(primary_key=True)
    address:Mapped[str] = mapped_column(nullable=False)
    start:Mapped[int] = mapped_column(nullable=False)
    seller_id:Mapped[int] = mapped_column(nullable=False)
    point:Mapped[int] = mapped_column(nullable=False)
    mdh:Mapped[str] = mapped_column(nullable=False)
    def __repr__(self): 
        return f"ID: {self.id} Address: {self.address} Start_time: {self.start}"

class Thong_ke(Base):
    __tablename__ = "thong_ke"
    id:Mapped[int] = mapped_column(primary_key=True)
    QR_created:Mapped[int] = mapped_column(nullable=False)
    QR_scanned:Mapped[int] = mapped_column(nullable=False)
    QR_active:Mapped[int] = mapped_column(nullable=False)
    bill_made:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self):
        return f"ID: {self.id} QR created: {self.QR_created} QR scanned: {self.QR_scanned} QR active: {self.QR_active}"
    
class User(Base, UserMixin):
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
    bill_code:Mapped[str] = mapped_column(nullable=False)
    time:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self) -> str:
        return f"id: {self.id} point_gained: {self.point_gained} time: {self.time} user_id: {self.user_id}"
class Notifi(Base):
    __tablename__ = "notifications"
    id:Mapped[int] = mapped_column(primary_key=True)
    time:Mapped[str] = mapped_column(nullable=False)
    text:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(nullable=False)

class Note(Base):
    __tablename__ = "notes"
    id:Mapped[int] = mapped_column(primary_key=True)
    items:Mapped[str] = mapped_column(nullable=False)
    time:Mapped[str] = mapped_column(nullable=False)
    location:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(nullable=False)

class Item(Base):
    __tablename__ = "items"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    giam:Mapped[str] = mapped_column(nullable=False)
    price:Mapped[int] = mapped_column(nullable=False)
    code:Mapped[str] = mapped_column(nullable=False)

class Trade_history_user(Base):
    __tablename__ = "trade_history_user"
    id:Mapped[int] = mapped_column(primary_key=True)
    point_paid:Mapped[int] = mapped_column(nullable=False)
    item_name:Mapped[str] = mapped_column(nullable=False)
    item_id:Mapped[int] = mapped_column(nullable=False)
    time:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(nullable=False)
    ma:Mapped[str] = mapped_column(nullable=False)