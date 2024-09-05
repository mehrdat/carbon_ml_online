from confluent_kafka import Consumer, KafkaError,Producer
import torch
import torch.nn as nn
import json
import requests
import pandas as pd
import numpy as np
from pandas import json_normalize
from utils import get_producer

producer = get_producer()
def produce_messages():
    for i in range(10):
        data={"message":f"test message{i}"}
        producer.produce("carbon",key=str(i),value=json.dumps(data))
        producer.flush()
    
if __name__=="__main__":
    produce_messages()
