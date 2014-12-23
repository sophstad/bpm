from flask import Flask, jsonify, render_template
from urllib2 import urlopen
import requests
import json
import csv
from jinja2 import Environment

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def data():
  url = "http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=sw1m97&api_key=dfc0d3f11ee15ab2f914558029a4896c&format=json&limit=50&period=1month"
  api = requests.get(url).json()
  return render_template('albums.html', artist_data=api)

@app.route("/search/<search_query>")
def search(search_query):
  return search_query

@app.errorhandler(404)
def page_not_found(error):
  return "Sorry, page not found", 404

if __name__ == "__main__":
  app.run(host="0.0.0.0")

'''
  def simplify():
    for artist, plays in the_data['weeklyartistchart']['artist']:
      yield artist['name'], plays
  artists = simplify()
'''