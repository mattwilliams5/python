#!/usr/local/bin/python

import json
import requests

api_token = 'af2cf77069e57c11c02163070ddb8d8886031c2a4d835184f5d7436851c0e71d'
api_url_base = 'https://api.digitalocean.com/v2/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

api_url = '{0}account'.format(api_url_base)
response = requests.get(api_url, headers=headers)

def get_account_info():

    api_url = '{0}account'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

    account_info = get_account_info()

    if account_info is not None:
        print("Here is your info: ")
        for k, v in account_info['account'].items():
            print('{0}:{1}'.format(k,v))
    else:
        print('[!] Request Failed')
