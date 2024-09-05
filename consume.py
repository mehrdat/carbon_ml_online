from confluent_kafka import Consumer, KafkaError,Producer
import torch
import torch.nn as nn
import json
import requests
import pandas as pd
import numpy as np
from pandas import json_normalize
from utils import get_producer,consumer,consume_messages


class CarbonLstm(nn.Module):
    pass



consumer=consumer()
def process_message(message):
    # data=json.loads(message)
    # print(f"message recieved {data}")
    
    

if __name__=="__main__":
    consume_messages(consumer,process_message)