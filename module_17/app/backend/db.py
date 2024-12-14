from sqlalchemy import create_engine, Column,  Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///taskmanager.db", echo = True)

Local_session = sessionmaker(bind = engine)

#Base = declarative_base()

class Base(DeclarativeBase):
    pass


