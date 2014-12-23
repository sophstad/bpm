from flask import Flask
import requests

url = "http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=sw1m97&api_key=dfc0d3f11ee15ab2f914558029a4896c&format=json"
response = requests.get(url)
response_dict = response.json

print response_dict