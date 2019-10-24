import requests


url = requests.get('https://api.github.com/')

json = url.json()

print(json)
