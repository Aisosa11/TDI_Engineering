from sqlalchemy import create_engine, ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy import create_engine
from decouple import config

Base = declarative_base()


class Person(Base):
    __tablename__= "tennis"

    ssn = Column("ssn",Integer,primary_key=True)
    firstname = Column ("firstname", String)
    lastname = Column ("lastname", String)



    def __init__(self,ssn,first,last):
        self.ssn = ssn
        self.firstname = first
        self.lastname =  last
    def __repr__(self):
        return f"({self.ssn}),({self.firstname}),({self.lastname})"

user = config("user")
passwd = config("passwd")
host = config("host")
port = config("port")
db = "tennis"

conn = psycopg2.connect(
    host=host,
    database=db,
    user=user,
    password=passwd,
    port = port)

engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(user, passwd, host, port,db))

Session = sessionmaker(bind=engine)
session = Session

session.add()
session.commit()