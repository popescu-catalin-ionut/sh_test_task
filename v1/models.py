# models.py
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

from common.settings import SECRET_KEY, SQLALCHEMY_DATABASE_URL

secret_key = SECRET_KEY
SQLALCHEMY_DATABASE_URL: str = SQLALCHEMY_DATABASE_URL
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    username = Column(String, index=True, unique=True)
    password = Column(StringEncryptedType(key=str(secret_key), engine=AesEngine, padding="pkcs5"))
    role = Column(Enum('admin', 'editor', name='user_roles'))
    genres = Column(String)


postgres_engine = create_engine(SQLALCHEMY_DATABASE_URL)
connection = postgres_engine.connect()
Session = sessionmaker(autocommit=False, autoflush=False, bind=postgres_engine)
session = Session()
Base.metadata.create_all(bind=postgres_engine)
