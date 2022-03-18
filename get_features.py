import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import matplotlib.pyplot as plt
import japanize_matplotlib

artist_url = "https://open.spotify.com/artist/38WbKH6oKAZskBhqDFA8Uj?si=rGUTeP3pS9W6U9pf4hAhDw"

my_id ='2ab3c7f06ff246e2b7ced6399709689d' #client ID
my_secret = 'c7c6568d53a04421a538612a6fcf3c3b' #client secret
ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)
results = spotify.artist_top_tracks(artist_url)

id_list = []
name_list = []

for result in results['tracks']:
    id_list.append(result['id'])
    name_list.append(result['name'])

results = spotify.audio_features(id_list)


music_list = []
idx = 0
plt.xlabel("valence")
plt.ylabel("arousal")
for result in results:
    music = {
        "name" : name_list[idx],
        "valence" : result['valence'],
        "energy" : result['energy']
    }
    music_list.append(music)
    plt.plot(result['valence'], result['energy'], 'o')
    plt.annotate(name_list[idx], xy=(result['valence'], result['energy']))
    idx += 1

plt.show()
