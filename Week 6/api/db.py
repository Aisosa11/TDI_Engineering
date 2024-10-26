import pandas as pd
import psycopg2
from decouple import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, text, select


user = config("user1")
passwd = config("passwd1")
host = config("host1")
port = config("port1")
db = config("db1")

# sqlalchemy
supabase_db_url = f"postgresql://{user}:{passwd}@{host}:5432/{db}"
engine = create_engine(supabase_db_url)
TennisBase = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

print('connected')

def get_db():
    db = SessionLocal()
    return db















"""
connection = psycopg2.connect(
    dbname=db,
    user=user,
    password=passwd,
    host=host,
    port=port
)













#engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(user, passwd, host, port,db))
engine = create_engine(f'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}')
#engine = create_engine(f'postgresql://postgres.lmwkdjyhamnuxygbbvqg:[YOUR-PASSWORD]@aws-0-eu-central-1.pooler.supabase.com:5432/postgres)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
TennisBase = declarative_base()

print('connected')

#def get_db():
 #   db = sessionlocal()
  #  return db  



from supabase import create_client, Client
import json
from decouple import config


def get_db():
    url = config("SUPABASE_URL")
    key = config("SUPABASE_KEY")
    supabase = create_client(url, key)
    return supabase.table("Tennis")  # Replace with your actual table name
"""
