#uses spotipy instead of spotify API
from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os

load_dotenv(find_dotenv())
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
app = Flask(__name__)

artistID = 'spotify:artist:0hCNtLu0JehylgoiP8L4Gh'
artist = 'Nicki Minaj'
top_tracks = sp.artist_top_tracks(artistID, country='US')

@app.route('/')
def ttt():
    tracks=[]
    previews=[]
    covers=[]
    for track in top_tracks['tracks'][:10]:
        tracks.append(track['name'])
        previews.append(track['preview_url'])
        covers.append(track['album']['images'][0]['url'])
    
    track = random.choice(tracks)
    index = tracks.index(track)
    preview = previews[index]
    cover = covers[index]
    
    return render_template(
        'index2.html',
        track=track,
        preview=preview,
        cover=cover,
        artist=artist,
        index=index
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)