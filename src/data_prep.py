from confluent_kafka import Consumer, KafkaError,Producer
import torch
import torch.nn as nn
import json
import requests
import pandas as pd
import numpy as np
from pandas import json_normalize
from sklearn.preprocessing import LabelEncoder

url_intensity="https://api.carbonintensity.org.uk/intensity"
url_factors="https://api.carbonintensity.org.uk/intensity/factors"

def get_data_from_api(url="https://api.carbonintensity.org.uk/intensity"):
    response=requests.get(url)
    response_factors=requests.get(url+'/factors')
    df_intensity=pd.json_normalize(response.json()['data'])
    df_factors=pd.json_normalize(response_factors.json()['data'])
    df=pd.concat([df_intensity,df_factors],axis=1)
    
    df=df.drop(['from'],axis=1)
    df=df.rename(columns={'to':"date",
                        "intensity.forecast":"forecast",
                        "intensity.actual":"actual",
                        "intensity.index":"index",
                        "Gas (Combined Cycle)":"Gas_combined",
                        "Gas (Open Cycle)":"Gas_open",
                        "Irish Imports":"Irish_imports",
                        "Pumped Storage":"Pumped_storage",
                        "Dutch Imports":"Dutch_imports",
                        "French Imports":"French_imports"})
    df=df.set_index("date")
    df['index']=LabelEncoder().fit_transform(df['index'])

    return df