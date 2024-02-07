import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


#*************** Scraping Billboard 100 ***************
date = input("Which year do you want to travel to?"
             "Type the date in this format YYYY-MM-DD: ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(BILLBOARD_URL).text
soup = BeautifulSoup(response, "html.parser")
all_songs = soup.select("li ul li h3")
songs = [songs.getText().strip() for songs in all_songs]

#*************** Spotify Auth ***************
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost",
        client_id="CLIENT ID",
        client_secret="CLIENT_SECRET KEY",
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#*************** Searching in Spotify ***************
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#*************** Create Playlist ***************
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#*************** Add song ***************
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("*********** END ************")
