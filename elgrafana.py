#!/usr/bin/python3

import requests
import json
from requests.exceptions import HTTPError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
now = datetime.now()

raw_data = requests.get("https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/channels")
json_data = raw_data.json()

streamingURLCount = 0
for i in range(len(json_data["channels"])):
    for j in range(len(json_data["channels"][i]["stationSchedules"])):
        for k in range(len(json_data["channels"][i]["stationSchedules"][j]["station"]["videoStreams"])):
            if json_data["channels"][i]["stationSchedules"][j]["station"]["videoStreams"][k]["streamingUrl"] != None:
                streamingURLCount = streamingURLCount + 1

el_datset = {}
el_datset["timestamp"] = now
el_datset["totalResults"] = json_data["totalResults"]
el_datset["streamingUrl"] = streamingURLCount

es_post_request = es.index(index='nld_channels', ignore=400, body=el_datset)

            
