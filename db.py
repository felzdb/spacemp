from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Defina suas credenciais de conexão
username = 'postgres'
password = '[AgyAx9.#rrFXnA('
host = '34.151.212.149'  # ou o endereço IP do seu servidor
port = '5432'       # porta padrão do PostgreSQL
database = 'plsql-agroassets'

# Crie a string de conexão
connection_string = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

# Crie o engine do SQLAlchemy
engine = create_engine(connection_string)

# Configure a base declarativa
Base = declarative_base()

# Crie uma fábrica de sessões
Session = sessionmaker(bind=engine)
