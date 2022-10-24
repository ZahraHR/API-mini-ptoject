# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:fatima@localhost:5432/movies')
Session = sessionmaker(bind=engine)

Base = declarative_base()
