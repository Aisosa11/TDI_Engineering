from sqlalchemy.orm import Session
from schema import NewPlayer  
from db import TennisBase
import model


#Get all Tennis data
def get_details(db:Session, skip:int=0,limit:int=100):
    return db.query(TennisBase).offset(skip).limit(limit).all()

#Get Result by ID 
def get_by_ID(db:Session, Tennis_id:int):
    return db.query(TennisBase).filer(Tennis_id ==TennisBase.id).first()


#Create a new Player Record
def create_new_player(db:Session,player:NewPlayer):
    new_player=TennisBase(**player.dict())
    db.add(TennisBase)
    db.commit()
    db.refresh(TennisBase)
    return TennisBase

#Remove Player stats

def remove_row(db: Session, id: int):
    _TennisBase = get_by_ID(db=db, id=id)
    db.delete(_TennisBase)
    db.commit() 

#Update Player Stats

def update_stats(db: Session, id: int, name: str,  roundId: int, player1Id : int, player2Id : int, 
                  tournamentId : int,   match_winner : int, result : str,  addition : int):
    
    _TennisBase = get_by_ID(db=db, id=id)

    _TennisBase.name =name
    _TennisBase.roundId = roundId
    _TennisBase.player1Id = player1Id 
    _TennisBase.player2Id = player2Id 
    _TennisBase.tournamentId = tournamentId   
    _TennisBase.match_winner = match_winner
    _TennisBase.result = result 
    _TennisBase.addition = addition

    db.commit()
    db.refresh(_TennisBase)
    return _TennisBase