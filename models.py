from sqlalchemy import Column, Integer, String
from db import Base  # Importa a Base do db.py
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(Base):
    __tablename__ = 'tbl_users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)

novo_usuario = Usuario(name='Nome', username='username', email='email@example.com', phone='54940028922', password=generate_password_hash('sua_senha'))
