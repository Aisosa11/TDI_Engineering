from sqlalchemy.orm import Session
from schema import NewPlayer  
from db import TennisBase
import model

def get_all_player(db:Session):
    result = db.query(model.Tennis).all()
    return result

# Get Result by ID
def get_by_ID(db: Session, tennis_id: int):
    result = db.query(model.Tennis).filter(model.Tennis.id == tennis_id).first()
    return result

# Create a new Player Record POST
def create_new_player(db: Session, player: NewPlayer):
    new_player = model.Tennis(
        id = player.id,
        date = player.date,
        roundId= player.roundId, 
        player1Id = player.player1Id,   
        player2Id = player.player2Id, 
        tournamentId = player.tournamentId,
        match_winner = player.match_winner,
        result = player.result, 
        addition = player.addition 
    )
    db.add(new_player)
    db.commit()
    db.refresh(new_player)  # Refresh the newly created object (optional)
    return new_player

# Remove Player stats
def remove_row (db: Session, tennis_id: int):
    result = db.query(model.Tennis).filter(model.Tennis.id == tennis_id).first()
    db.delete(result)
    db.commit()        
    return {"status":"Successfully deleted"}

# Update Player Stats
def update_stats(db: Session, player: NewPlayer, tennis_id: int):
    result = db.query(model.Tennis).filter(model.Tennis.id == tennis_id).first()
    result.date = player.date,
    result.roundId= player.roundId,
    result.player1Id = player.player1Id,   
    result.player2Id = player.player2Id, 
    result.tournamentId = player.tournamentId,
    result.match_winner = player.match_winner,
    result.result = player.result, 
    result.addition = player.addition 
    db.commit()
    db.refresh(result) 
    return result 