from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# url
url = "mongodb+srv://eshantsingh552_db_user:TJ0eOf9aKmEu4Dkz@cluster0.ob9kjos.mongodb.net/?appName=Cluster0"

# create a new client and connect to server
client = MongoClient(url)

# create a database name and collection name

DATABASE_NAME = "pwskills"
COLLECTION_NAME = "wafer-fault"

df = pd.read_csv("D:\ML Projects\Sensor Fault Detection Project\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis=1)

json_record= list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)