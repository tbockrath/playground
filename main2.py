import json

import pandas as pd
import requests
from kafka import KafkaProducer

# KAFKA_ZOOKEEPER_CONNECT localhost:2181
# KAFKA_ADVERTISED_HOST_NAME kafka
def main():
    print("Starting App")

    data = getJsonData()
    #dF = pd.DataFrame.from_dict(data)
    #dF.to_csv('out.csv')
    #print(dF)

    print(data['aircraft'])


def getJsonData():
    host = 'http://192.168.2.115'
    port = '8080'
    url = '/data/aircraft.json?_='
    url_data = host +":" + port + url
    return requests.get(url_data).json()

def publishData(data):
    broker = '192.168.2.104'
    port = ''
    topic = 'adsb'
    producer = KafkaProducer(bootstrap_servers=[broker + ':'+ port])
    future = producer.send(topic, data)
    print('future', future)




if __name__ == "__main__":
    main()
