from sqlalchemy import create_engine, ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy import create_engine
from decouple import config
from api.db import Base

class Tennis_Base(Base):
    __tablename__ ='tennis'
    id = Column(BigInteger, primary_key=True, nullable=False)
    date = Column(DateTime)
    roundId = Column(Integer) 
    player1Id = Column(Integer) 
    player2Id = Column(Integer)
    tournamentId = Column(Integer)
    match_winner = Column(Integer)
    result = Column(Integer)
    addition = Column(Integer)
    

Base = declarative_base()
#!/usr/bin/python3
""" Models for connection to Postgres DB """

from sqlalchemy import (
    ARRAY,
    BigInteger,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base

TennisBase = declarative_base()


class Tennis(TennisBase):
    """

    """

    __tablename__ = "tennis_stats"

    id = Column(BigInteger, primary_key=True, nullable=False)
    date = Column(DateTime)
    roundId = Column(Integer) 
    player1Id = Column(Integer) 
    player2Id = Column(Integer)
    tournamentId = Column(Integer)
    match_winner = Column(Integer)
    result = Column(Integer)
    addition = Column(Integer)
