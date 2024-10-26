from sqlalchemy import create_engine, ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.orm import sessionmaker
import psycopg2
from sqlalchemy import create_engine
from datetime import datetime
from decouple import config
from db import TennisBase


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
    result = Column(String)
    addition = Column(Integer)