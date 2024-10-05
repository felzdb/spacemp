from sqlalchemy import Column, Integer, String
from db import Base  # Importa a Base do db.py

class Usuario(Base):
    __tablename__ = 'tbl_users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)

