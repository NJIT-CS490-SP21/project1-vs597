from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import requests
import os
import json

load_dotenv(find_dotenv())

#connecting to API
auth_url='https://accounts.spotify.com/api/token'
response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET')
})
json_response = response.json()
access_token = json_response['access_token']

app = Flask(__name__)

artist_id='0hCNtLu0JehylgoiP8L4Gh'
spot_url='https://api.spotify.com/v1/artists/'+artist_id+'/top-tracks?market=US'    #artist=nicki minaj
market='market=US'
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

music=requests.get(spot_url, headers=headers)
top_tracks = music.json()
tracks=[]
track_images={}

@app.route('/')
def topten():
    for track in range(0,10):
        tracks.append(top_tracks['tracks'][track]['name'])
        track_images[track] = top_tracks['tracks'][track]['album']['images'][0]['url']
    print("track images values: \n" +str(list(track_images)))
    
    return render_template(
        'index.html', 
        tracks=tracks,
        track_images=track_images,
        artist = 'Nicki Minaj',
        tracklen = len(tracks),
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)