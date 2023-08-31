import requests

response = requests.get('https://www.bbc.com/news')

print(response.status_code)