
**DATA PIPELINES AND EXTRACTION FROM API USING PREFECT AND POSTGRES**

   In this project, after retrieving data using RapidAPI, data was saved into a dataframe, the data saved was cleaned and then 
   saved in different file formats. This saved data was also linked into a database(postgress to be precise), this was done with 
   the aid of sqlaclchemy and with prefect I was able to create flows and keep the script running at specific given intervals. 

**AIM**
- To practice how to use sqlalchemy to link databases with python.
- To learn how to extract data from website and put into a dataframe and link it to your database.
- Learn about ETL processes.
- Learn how to use and setup virtual environments
- Learn how to save files extracted from website in different formats.

**REQUIREMENT**
- RapidAPI sign-in and subcription
- Prefect
- Postgress
- Installing and Importing of the below libraries and software:
   - requests
   - json
   - datetime
   - pyarrow
   - pandas
   - openpyxl
   - pyarrow
   - python-decouple
   - sqlalchemy
   - psycopg2
   - pandas
   - prefect

**PROCEDURE**
 - After subscribing to RAPIDAPI,
 - Install all required libraries and software.
 - Create an env file to store API key
 - Use of datetime and strip function to create different files when new information is retrieved from the website.
 - Save file in both XSLX and parquet formats.
 - Use the Conn function to create a connection with your database.
 - Defined Data structure on Postgress
 - Save dataframe into sql
 - Use the Prefect to create flows


 **Challenges/What I learnt**

Potential issues/challenges you might experience that I experienced:

 - Using the wrong format for datetime will return an error, so you have to use the strip functions to remove the spaces and also 
   change the format from having : or .
 - If the format of the data you are retrieving from the internet has a different format from the structure created on your 
   database, there is a high tendency that it will override the existing structure on your database table.
 - While using prefect, it is adviced that you use a virtual environment to help save system memory.
 - I was able to learn about ETL process and database connection.
 - I learnt how to perform basic data cleaning procedures using python.