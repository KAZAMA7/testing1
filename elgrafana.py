#!/usr/bin/python3
import requests
import json
from requests.exceptions import HTTPError
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://206.81.21.210:9200")

raw_data = requests.get("https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/channels")
json_data = raw_data.json()
es_post_request = es.index(index='nld_channels', ignore=400, body=json_data)

print(es_post_request)