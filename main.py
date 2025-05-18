#!/usr/bin/env python3

# Script that puts torrent files in the proper folders using Torrent Tags
# so movie torrents would be put in the movies folder, ect.

# Author : Nolan Winsman
# Date : 2025-05-18


import qbittorrentapi # pip install qbittorrent-api
from datetime import datetime

# documentation to API
# https://qbittorrent-api.readthedocs.io/en/latest/introduction.html

CATEGORIES = set()
DELETE_FILES = True
THRESHOLD = 90 # will delete any torrent older than this many days

# dictionary to map torrent tags to folders
# the key is the torrent tag and the value is the folder it should be put in
def main():

    today = datetime.today()

    # instantiate a Client using the appropriate WebUI configuration
    # change information to fit your login
    qbt_client = qbittorrentapi.Client(
        host='localhost',
        port=8080,
        username='admin',
        password='adminadmin'
    )

    # the Client will automatically acquire/maintain a logged in state in line with any request.
    # therefore, this is not necessary; however, you many want to test the provided login credentials.
    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)

    CATEGORIES.add('tv-sonarr')
    CATEGORIES.add('radarr')

    count = 0
    # retrieve all torrents and set their download folder to the corresponding tag
    for torrent in qbt_client.torrents_info():
        dt = datetime.fromtimestamp(torrent.added_on)
        added_on = dt.strftime("%m/%d/%Y")
        c = torrent.category

        if (today - dt).days > THRESHOLD and c in CATEGORIES:
            count +=  1
            print("Added Greater than 90 days ago and category matches")
            print(f"Added On: {added_on}\n")
            print(f'DELETING {torrent.name} ({c}) ({torrent.state}) ({torrent.tags})')
            qbt_client.torrents_delete(delete_files=DELETE_FILES, torrent_hashes=torrent.hash)

            

    print(f"Deleted {count} Torrents")

if __name__ == "__main__":
    main()
