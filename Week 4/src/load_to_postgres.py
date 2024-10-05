import pandas as pd
import psycopg2
from decouple import config
import requests
from sqlalchemy import create_engine
from datetime import datetime
from prefect import flow, task
from prefect.client.schemas.schedules import IntervalSchedule


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

#engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(user, passwd, host, port,db))
engine = create_engine(f'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}')

print('connected')

def request_url(url,headers):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    df_data = response.json()
    return df_data

def transform_data(df_data):
   return pd.DataFrame(df_data['data'])

"""
def save_to_db(df):
    engine = create_engine(f'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}')

    # Check if the table exists
    with engine.connect() as conn:
        if not conn.dialect.has_table(conn, 'tennis_players_ranking'):
            df.to_sql('tennis_players_ranking', engine, index=False, if_exists='fail')
        else:
            # Add a timestamp column
            df['created_at'] = datetime.now()
            df.to_sql('tennis_players_ranking', engine, if_exists='append', index=False)
"""




if __name__ == "__main__":
  url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/ranking/doubles/"

  headers = {
    "x-rapidapi-key": config("api_key"),
    "x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
  }  
  data = request_url(url,headers)
  transforms = transform_data(data)
  print(f'This is data {transforms}')
  df2 = pd.json_normalize(transforms['player'])
  transforms = transforms.drop(['player','wk'], axis = 'columns')
  df2.columns = df2.columns.str.replace(".", "_")
  transformed_data = pd.concat([transforms, df2], axis=1)
  transformed_data.to_sql('tennis_players_ranking', engine, if_exists='replace', index=False)

  print('Data saved successfully!')


