from confluent_kafka import Consumer, KafkaError,Producer
import torch
import torch.nn as nn
import json
import requests
import pandas as pd
import numpy as np
from pandas import json_normalize
from data_prep import get_data_from_api

df=get_data_from_api(url_intensity)

def get_producer():
    conf={"bootstrap.servers":"localhost:9092"}
    producer=Producer(**conf)
    topic="carbon"
    return producer


def consumer(group_id="group1",topic="carbon"):
    conf={
        "bootstrap.servers":"localhost:9092",
        "group.id":group_id,
        "auto.offset.reset":"earliest",
        }
    consumer=Consumer(**conf)
    consumer.subscribe([topic])
    return consumer

def consume_messages(consumer,callback):
    
    while True:
        msg=consumer.poll(0)
        if msg is not None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
            
        callback(msg.values().decode('utf-8'))
