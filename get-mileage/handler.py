import requests
import json
import os
from prettytable import PrettyTable

def handle(st):
    traveldata = PrettyTable(['Date','Starting Point','Ending Point','Miles Traveled'])
    j = json.loads(st)
    for i in j:
	    api_key = os.environ['gm_apikey']
        base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        payload = {
            'origins' : '|'.join([i['start']]),
            'destinations' : '|'.join([i['end']]), 
            'mode' : 'driving',
            'units': 'imperial',
            'api_key' : api_key
        }
        r = requests.get(base_url, params = payload)
        traveldata.add_row(
            (i['date'],
            r.json()['origin_addresses'][0],
            r.json()['destination_addresses'][0],
            r.json()['rows'][0]['elements'][0]['distance']['text'])
            )
        print(i)
    print(traveldata)
