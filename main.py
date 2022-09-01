import json
import requests

from refresh import Refresh
from secrets import spotify_user_id, daily_mix_ids

class DailyMix:
    def __init__(self):
        self.refresh = Refresh()
        self.spotify_token = self.refresh.refresh()
        self.user_id = spotify_user_id
        self.daily_mix_ids = daily_mix_ids
        self.new_playlist_id = ""
        self.daily_mix_playlist_id = ""

    def main(self):
        playlist_exists = False
        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"

        response = requests.get(query,headers={
            "Content-Type": "applications/json",
            "Authorization": f"Bearer {self.spotify_token}"})

        response_json = response.json()

        for i in response_json['items']:
            if "Daily Mix🔀" in i['name']:
                print("Playlist already exists......")
                self.daily_mix_playlist_id = i['id']
                playlist_exists = True

        if playlist_exists==False:
            self.create_playlist()
            self.add_to_playlist(self.new_playlist_id)
        
        else:
            self.empty_playlist(self.daily_mix_playlist_id)
            self.add_to_playlist(self.daily_mix_playlist_id)

    def add_to_playlist(self, playlist_id):
        print('Getting tracks from daily mixes...')
        for id in self.daily_mix_ids:
            tracks = []
            query = f"https://api.spotify.com/v1/playlists/{id}/tracks"

            response = requests.get(query, headers={
                "Content-Type": "applications/json",
                "Authorization": f"Bearer {self.spotify_token}"})

            response_json = response.json()

            for i in response_json['items']:
                tracks.append(i["track"]["uri"])
        
            self.add_tracks(','.join(tracks), playlist_id)

    def add_tracks(self, tracks, playlist_id):        
        print("Adding songs.....")
        query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?uris={tracks}"

        requests.post(query, headers={
                "Content-Type": "applications/json",
                "Authorization": f"Bearer {self.spotify_token}"})

    def create_playlist(self):
        print("Creating New Playlist......")
        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"

        request_body =  json.dumps({
            "name": "Daily Mix🔀",
            "description": "All daily mixes created by Spotify. Updates everyday."
            })

        response = requests.post(query, data=request_body, headers={
                "Content-Type": "applications/json",
                "Authorization": f"Bearer {self.spotify_token}"})

        response_json = response.json()
        self.new_playlist_id = response_json["id"]
    
    def empty_playlist(self, id):
        query = f"https://api.spotify.com/v1/playlists/{id}/tracks?uris={''}"

        requests.put(query, headers={
            "Content-Type": "applications/json",
            "Authorization": f"Bearer {self.spotify_token}"})


if __name__ == '__main__':
    obj = DailyMix()
    obj.main()
