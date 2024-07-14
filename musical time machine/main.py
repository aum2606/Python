from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

SPOTIFY_CLIENT_ID = "YOUR CLIENT ID"
SPOTIFY_CLIENT_SECRET = "YOUR CLIENT SECRET"
SPOTIFY_NAME = "YOUR NAME"

date = input("Which year you want to travel to ? (Enter date in YYYY-MM-DD format): ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text,'html.parser')
song_names_spans = soup.select("li ul li h3")
# print(song_names_spans)
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username= SPOTIFY_NAME
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uri = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} BillBoard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uri)


