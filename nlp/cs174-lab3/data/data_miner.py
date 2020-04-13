import lyricsgenius
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

ID_ = 'aaa2cbeb962e4a40b548e33907dc8e3f'
SECRET = 'c06e04251471422997c3f878c3b05e94'

# Gets the credentials from the environment variables. Make sure that SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
# are in your environment.
ccm = SpotifyClientCredentials(client_id=ID_, client_secret=SECRET)
sp = spotipy.Spotify(client_credentials_manager=ccm)

PLAYLIST_URI = 'spotify:playlist:0fLLZQlgUdCUbfiDZ3kJq7'
NUM_TRACKS = 20

def edit_title(title):
    if title == 'You Make My Dreams - Remastered':
        return 'You Make My Dreams'
    elif title == 'Let It Be - Remastered 2009':
        return 'Let It Be'
    elif title == "Don't Stop Me Now - 2011 Mix":
        return "Don't Stop Me Now"
    else:
        return title

# Will modify the dictionary so as to include the artist as well as the song title.
# The structure will be a dictionary of two-element tuples. Example: {1 : ('Take On Me', 'a-ha')}

playlist_tracks = sp.playlist_tracks(PLAYLIST_URI)['items']
playlist_dict = {}
for i, track in enumerate(playlist_tracks[:NUM_TRACKS]):
    title = track['track']['name']
    title = edit_title(title)
    artists = ', '.join([artist['name'] for artist in track['track']['artists']])
    playlist_dict[i] = (title, artists)

#print(playlist_dict)
songtitles = [playlist_dict[x][0] for x in playlist_dict]
songtitles

songs = playlist_dict
lyrics_dict = {}
genius = lyricsgenius.Genius("lgrmQD5L0EqGrGCqmiXmHvizYtaDYeu5gAn0TRwD3FPEzE1WRL_Y2mBAZTdrMGB-")

for song in songs:
    lyric = genius.search_song(songs[song][0], songs[song][1])
    #print(lyric.lyrics,"\n")
    lyrics_dict[songs[song]] = lyric.lyrics

#print(lyrics_dict)

#with open('file.txt', 'w') as file:
    #file.write(json.dumps(lyrics_dict))

with open('lyrics_file.txt', 'w') as f:
    print(lyrics_dict, file = f)