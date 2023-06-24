from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer
from typing import List
class Base(DeclarativeBase):
    pass
class Seller(Base):
    __tablename__ = "sellers"
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    qr_made:Mapped[int] = mapped_column(nullable=False)   
    links_points:Mapped[List["Links_point"]] = relationship(back_populates = 'seller')
    #
    def __repr__(self):
        return f"ID: {self.id} Name: {self.name} QR_made: {self.qr_made}"   
###
class Links_point(Base):
    __tablename__ = "links_point"
    id:Mapped[int] = mapped_column(primary_key=True)
    address:Mapped[str] = mapped_column(nullable=False)
    start:Mapped[int] = mapped_column(nullable=False)
    #seller_id:Mapped[int] = mapped_column(ForeignKey('sellers.id'))
    seller_id:Mapped[int] = mapped_column(ForeignKey('sellers.id'))
    seller:Mapped["Seller"] = relationship(back_populates = 'links_points')
    #
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
    point:Mapped[int] = mapped_column(nullable=False)
    def __repr__(self):
        return f"id: {id} username: {self.username} password: {self.password} point: {self.point}"