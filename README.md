![image](https://user-images.githubusercontent.com/88645471/213471635-e5d7e10b-551a-4ef9-b473-b0aa6183bf61.png)

# Overview
This is a python script that combines all six daily mix playlists created by Spotify and merges then into a single playlist. It can be automated using PythonAnywhere (www.pythonanywhere.com) or the Windows Task Scheduler to run every day at a specific time.

# Installation
Clone the repository by `git clone https://github.com/dcsp3/daily-mix-spotify.git`

# Usage
1. Create an app using the Spotify developer dashboard
2. Authorize this app using the documentation from Spotify
3. Get the refresh token and save it in secrets.py
4. Get playlist ids of all 6 daily mix playlists and save them in secrets.py
5. Automate using python anywhere/task scheduler.

# References
- Spotify Developer Dashboard - https://developer.spotify.com/dashboard
- Spotify App Authorization - https://developer.spotify.com/documentation/general/guides/authorization/
- Creating Playlist - https://developer.spotify.com/documentation/web-api/reference/#/operations/create-playlist
- Getting Playlist Items - https://developer.spotify.com/documentation/web-api/reference/#/operations/get-playlists-tracks
- Adding Items to Playlist - https://developer.spotify.com/documentation/web-api/reference/#/operations/add-tracks-to-playlist
