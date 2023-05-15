import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()


data = main_request(baseurl, endpoint)

pages = data['info']['pages']

name = data['results'][0]['name']

episodes = data['results'][0]['episode']

print(name)