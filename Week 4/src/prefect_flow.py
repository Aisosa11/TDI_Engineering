from prefect import flow, task
import pandas as pd 
from decouple import config
from sqlalchemy import create_engine
import requests
import os
import psycopg2
from datetime import datetime, timedelta
from prefect.client.schemas.schedules import IntervalSchedule
from datetime import timedelta, datetime



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


engine = create_engine(f'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}')

print('connected')

@flow
def fetch_and_save_to():
    url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/ranking/doubles/"
    headers = {
        "x-rapidapi-key": config("api_key"),
        "x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
    }

    @task
    def fetch_data():
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")

    @task
    def transform_data(data):
        return data['data']

    @task
    def process_data(data):
        df2 = pd.json_normalize(data['player'])
        data = data.drop(['player', 'wk'], axis='columns')
        df2.columns = df2.columns.str.replace(".", "_")
        transformed_data = pd.concat([data, df2], axis=1)
        return transformed_data

    @task(docstring="Saves DataFrame to CSV and Parquet files in specified folder")
    def save_to(data:pd.DataFrame, folder = "datalake"):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        try:
            data.to_csv(f'{folder}/tennis.{timestamp}.csv',index=False)
            data.to_parquet(f'{folder}/tennis.{timestamp}.parquet',index=False)
        except Exception as e:
            print(f"Invalid URL {e}")
    
    @task
    def  save_to_db(df):
         processed_data.to_sql('tennis_players_ranking', engine, if_exists='replace', index=False)



    data = fetch_data()
    transformed_data = transform_data(data)
    processed_data = process_data(transformed_data)
    save_to(processed_data)
    save_to_db(processed_data)
    print('Data saved successfully!')



if __name__ == "__main__":
    # Schedule the flow to run every 33 minutes (adjust as needed)
     fetch_and_save_to.serve(schedule = [
     IntervalSchedule(
       interval=timedelta(seconds=1000),
        anchor_date=datetime(2024, 10, 5),
        timezone="America/Chicago"
        )
    ]
    )
#    fetch_and_save_to.serve(schedules=[schedule])

"""
if __name__ == "__main__":
    # Schedule the flow to run every 60 seconds (1 minute)
    schedule =IntervalSchedule(
        interval=timedelta(seconds=2000),
        anchor_date=datetime(2024, 10, 5),  # Initial run on October 5, 2024
        timezone="America/Chicago"
    )

    fetch_and_save_to.serve(schedules=[schedule])


#if __name__ == "__main__":
#fetch_and_save_to()
"""