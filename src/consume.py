from confluent_kafka import Consumer, KafkaError,Producer
import torch
import torch.nn as nn
import json
import requests
import pandas as pd
import numpy as np
from pandas import json_normalize
from utils import get_producer,consumer,consume_messages

device="cpu"
class CarbonLstm(nn.Module):
    def __init__(self,input_size,hidden_size,output_size,num_layers=1):
        super(CarbonLstm,self).__init__()
        self.lstm=nn.LSTM(input_size,hidden_size,num_layers,batch_first=True)
        self.linear=nn.Linear(hidden_size,output_size)
    
    def forward(self,x):
        h_0=torch.zeros(1,x.size(0),hidden_size).to(device)
        c_0=torch.zeros(1,x.size(0),hidden_size).to(device)
        out,_=self.lstm(x,(h_0,c_0))
        out=self.linear(out[:,-1,:])
        return out

input_size = 2
hidden_size = 50
output_size = 1
num_layers = 1


model=CarbonLstm(input_size,hidden_size,output_size)
criterion=nn.MSELoss()
optimizer=torch.optim.AdamW(model.parameters(),lr=0.001)


def process_message(message):
    # data=json.loads(message)
    # print(f"message recieved {data}")
    try:
        data=json.loads(message)
        data=pd.DataFrame([data])
        input_tensor=torch.tensor(data.drop(['actual'],axis=1).values,dtype=torch.float32)
        target_tensor=torch.tensor(data['actual'].values,dtype=torch.float32)
        
        model.train()
        optimizer.zero_grad()
        output=model(input_tensor)
        loss=criterion(output,target_tensor)
        
        loss.backward()
        optimizer.step()
        
        
        
    except (KeyError,TypeError,ValueError) as e:
        print(f"Error processing message {e}")
        
consumer=consumer()

if __name__=="__main__":
    consume_messages(consumer,process_message)