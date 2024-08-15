import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Remplacez ces valeurs par vos informations
CLIENT_ID = 'your_client_ID'
CLIENT_SECRET = 'Secret_Token_provided'
REDIRECT_URI = 'URI_defined_on_Dashboard'
SCOPE = 'playlist-read-private'

# Authentification avec Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# Récupération des playlists de l'utilisateur
def get_playlists():
    results = sp.current_user_playlists()
    playlists = results['items']
    
    with open('playlists.txt', 'w', encoding='utf-8') as file:
        for playlist in playlists:
            file.write(f"Playlist : {playlist['name']}\n")
            file.write(f"  ID : {playlist['id']}\n")
            file.write(f"  URL : {playlist['external_urls']['spotify']}\n")
            file.write('\n')

if __name__ == "__main__":
    get_playlists()
    print("Les playlists ont été sauvegardées dans le fichier 'playlists.txt'.")
