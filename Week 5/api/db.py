import pandas as pd
import psycopg2
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


user = config("user")
passwd = config("passwd")
host = config("host")
port = config("port")
db = config("db")

conn = psycopg2.connect(
    host=host,
    database=db,
    user=user,
    password=passwd,
    port = port)

#engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(user, passwd, host, port,db))
engine = create_engine(f'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}')

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

TennisBase = declarative_base()

print('connected')

