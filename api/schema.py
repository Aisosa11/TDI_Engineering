from pydantic import BaseModel
from datetime import datetime 

class NewPlayer(BaseModel):
    id: int
    date: datetime
    roundId: int 
    player1Id : int 
    player2Id : int
    tournamentId : int
    match_winner : int
    result : str
    addition : int
