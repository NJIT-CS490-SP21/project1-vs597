from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import requests
import os
import random

load_dotenv(find_dotenv())

#connecting to API
auth_url='https://accounts.spotify.com/api/token'
response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('SPOTIPY_CLIENT_ID'),
    'client_secret': os.getenv('SPOTIPY_CLIENT_SECRET')
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
track_images=[]
preview=[]
artists=[]

@app.route('/')
def topten():
    for i in range(0,10):
        tracks.append(top_tracks['tracks'][i]['name'])
        track_images.append(top_tracks['tracks'][i]['album']['images'][0]['url'])
        preview.append(top_tracks['tracks'][i]['preview_url'])
        artists.append(top_tracks['tracks'][i]['album']['name'])
    #print("artists: \n"+str(artists))
    track=random.choice(tracks)
    index=tracks.index(track)
    
    return render_template(
        'index.html', 
        index=index,
        track=track,
        track_image=track_images[index],
        preview=preview[index],
        artist=artists[index],
    )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)