from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import model
from db import engine, SessionLocal
from sqlalchemy.orm import Session
from schema import NewPlayer
import Crud
from model import Tennis
import uvicorn

app = FastAPI()

#model.TennisBase.metadata.create_all(bind = engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends (get_db)]

@app.get("/players")
async def get_allplayers(db: db_dependency):
    result = Crud.get_all_player(db)
    return result

@app.post("/Create")
async def create_new_player_stats(db: db_dependency, player: NewPlayer):
    new_player = Crud.create_new_player(db, player)
    return new_player

@app.get("/Player/{tennis_id}")
async def get_stats(db: db_dependency,tennis_id:int ):
    result = Crud.get_by_ID(db, tennis_id) 
    return result

@app.put("/Update/{tennis_id}")
async def get_update_stats(db:db_dependency,player:NewPlayer,tennis_id:int):
    result= Crud.update_stats (db, player,tennis_id)
    return result


@app.delete("/delete/{tennis_id}")
async def delete_player_stats(db:db_dependency, tennis_id):
    result = Crud.remove_row(db, tennis_id)
    return result




if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) #Used to run file on server
