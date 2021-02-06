from dotenv import load_dotenv, find_dotenv
import requests
import os
import json

load_dotenv(find_dotenv())
auth_url='https://accounts.spotify.com/api/token'
# data = {
#     'grant_type': 'client_credentials',
#     'client_id': os.getenv('CLIENT_ID'),
#     'client_secret': os.getenv('CLIENT_SECRET')
# }
    
response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
})
json_response = response.json()
access_token = json_response['access_token']

url='https://api.spotify.com/v1/artists/0hCNtLu0JehylgoiP8L4Gh/top-tracks?market=US'    #artist=nicki minaj
#artist_id='0hCNtLu0JehylgoiP8L4Gh?si=5NaHOy9LQhi7JY-kCSgAvw'
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

music=requests.get(url, headers=headers)
#print(music.content)
top_tracks = music.json()

for track in range(0,10):
    print(top_tracks['tracks'][track]['name'])
    
