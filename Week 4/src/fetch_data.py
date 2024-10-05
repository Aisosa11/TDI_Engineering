import pandas as pd 
from datetime import datetime
from decouple import config
from sqlalchemy import create_engine
import requests
import os
from prefect import flow, task


def request_url(url,headers):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    df_data = response.json()
    return df_data

def transform_data(df_data):
   return pd.DataFrame(df_data['data'])

def save_to(data:pd.DataFrame, folder = "datalake"):
  try:
     data = pd.DataFrame(data)
     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
     data.to_csv(f'{folder}/tennis.{timestamp}.csv',index=False)
     data.to_parquet(f'{folder}/tennis.{timestamp}.parquet',index=False)
  except Exception as e:
     print(f"Invalid URL {e}")

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
  transformed_data = pd.concat([transforms,df2], axis = 1)
  save_to(transformed_data)
