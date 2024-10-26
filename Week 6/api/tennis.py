import pandas as pd
import requests
import argparse
from decouple import config
from datetime import datetime
from prefect import flow, task
from datetime import timedelta, datetime
from prefect.client.schemas.schedules import IntervalSchedule
from model import Tennis
from db import get_db
import random

#@task
def forever() -> pd.DataFrame:

    url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/h2h/matches/5992/677/"

    headers = {
        "x-rapidapi-key": config('api_key'),
        "x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()['data']

    df = pd.DataFrame(data)

    return df

#@task
def clean(df: pd.DataFrame) -> pd.DataFrame:
    print(df.columns) 
    # TODO: algorithms to clean data based on specific needs
    df = df
    return df

#@task
#def store(df: pd.DataFrame) -> None:
    # df.to_parquet(f'./tennis_{datetime.now()}.parquet', index=True)
    # TODO: configure proper naming conventions
    #df.to_csv(f'./tennis_{datetime.now()}.csv')
def store(df: pd.DataFrame) -> None:
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'./tennis_{now}.csv'
    df.to_csv(filename)
#@task
def upload_db(df: pd.DataFrame) -> None:

    tennis_db = get_db()
    db_data = [
                Tennis(
                    id = random.randint(100000000, 1000000000000000000),
                    date = row["date"],
                    roundId = row["roundId"],
                    player1Id = row["player1Id"],
                    player2Id = row["player2Id"],
                    tournamentId = row["tournamentId"],
                    match_winner = row["match_winner"],
                    result = row["result"],
                    addition = row["player1Id"] + row["tournamentId"]
                )
                for row in df.to_dict(orient='records')
        ]
    tennis_db.add_all(db_data)
    tennis_db.commit()
    
    
#@flow
def main():
    data = forever()
    cleaned_data = clean(data)
    store(cleaned_data)
    upload_db(cleaned_data)

if __name__=='__main__':
    main()

"""
if __name__=='__main__':
    main.serve(schedules=[
    IntervalSchedule(
      interval=timedelta(seconds=60),
        anchor_date=datetime(2024, 10, 5),
        timezone="America/Chicago"
        )
    ]
    )
    # main()
"""