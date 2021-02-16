#uses spotipy instead of spotify API
from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os
import requests

load_dotenv(find_dotenv())

#using spotipy to get top tracks for artist Nicki Minaj
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
app = Flask(__name__)

artistID = 'spotify:artist:0hCNtLu0JehylgoiP8L4Gh'
artist = 'Nicki Minaj'
top_tracks = sp.artist_top_tracks(artistID, country='US')

#authorizing genius api to get lyrics url
search_url = 'https://api.genius.com/search?'
headers = {'Authorization': 'Bearer ' + os.getenv('GENIUS_ACCESS_TOKEN')}

@app.route('/')
def ttt():
    tracks=[]
    previews=[]
    covers=[]
    artists=[]
    
    for track in top_tracks['tracks'][:10]: #getting top tracks' information and organizing it into lists
        tracks.append(track['name'])
        previews.append(track['preview_url'])
        covers.append(track['album']['images'][0]['url'])
        artists.append(track['album']['artists'][0]['name'])
    
    track = random.choice(tracks)
    index = tracks.index(track)
    preview = previews[index]
    trackArtist = artists[index]
    cover = covers[index]
    
    data = {'q': track+' '+artist}
    response = requests.get(search_url, data=data, headers=headers)
    json_response = response.json()
    song = None

    for hit in json_response['response']['hits']:
        if trackArtist.lower() in hit['result']['primary_artist']['name'].lower(): #if the track names are the same
            song = hit['result']['url'] #url for lyrics
            break
    
    return render_template(
        'index2.html',
        track=track,
        preview=preview,
        cover=cover,
        trackArtist=trackArtist,
        index=index,
        song=song,
    )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)