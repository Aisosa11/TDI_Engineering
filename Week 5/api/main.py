from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import model
from db import engine, sessionlocal
from sqlalchemy.orm import Session
from schema import NewPlayer
import Crud
from model import TennisBase
app = FastAPI()

model.TennisBase.metadata.create_all(bind = engine)



def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends (get_db)]

"""
@app.post("/New_Player/")
async def New_player(player:NewPlayer,db= db_dependency):
    Db_newplayer = model.newplayer(player_new=player)
    db.add(Db_newplayer)
    db.commit() 
    db.refresh(Db_newplayer)
"""


@app.post('/Create')
async def create_new_player_stats(player:NewPlayer,db:db_dependency):
    Crud.create_new_player(db,player=NewPlayer)
    return {"status":"success"}


@app.get("/")
async def get_stats( db:db_dependency,skip:int=0,limit:int=1000,):
    _TennisBase =Crud.get_details(db,skip,limit)
    return {"status":"success"}


@app.put("/Update")
async def get_update_stats(player:NewPlayer,db:db_dependency):
    _TennisBase= Crud.update_stats (db, player)
    return {"status":"success"}


@app.delete("/delete")
async def delete_player_stats(player_id:NewPlayer,db:db_dependency):
    Crud.remove_row(db,player_id)
    return {"status":"success"}   

