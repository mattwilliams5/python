#!/usr/local/bin/pythonimport json
import requests

api_token = 'af2cf77069e57c11c02163070ddb8d8886031c2a4d835184f5d7436851c0e71d'
api_url_base = 'https://api.digitalocean.com/v2/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_ssh_keys():
    api_url = '{0}account/keys'.format(api_url_base)
    response = requests.get(api_url, headers=headers)
    if response.status_code >= 500:
        print('[!] [{0}] Server Errror'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
    elif response.status_code == 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
    elif response.status_code == 200:
        ssh_keys = json.loads(response.content.decode('utf-8'))
        return ssh_keys
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Contect: {1}'.format(response.status_code, response.content))

    add_response = add_ssh_keys('tutorial_key','/Users/mattw/.ssh/dc.pub')
    if add_response is not None:
        print('Your key was added: ')
        for k, v in add_response.items():
            print('  {0}:{1}'.format(k,v))
        else:
            print('[!] Request Failed')
get_ssh_keys()
