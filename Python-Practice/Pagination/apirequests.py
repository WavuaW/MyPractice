import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()

def get_pages(response):
    return response['info']['pages']


data = main_request(baseurl, endpoint)
print(get_pages(data))



name = data['results'][0]['name']

episodes = data['results'][0]['episode']

print(name)