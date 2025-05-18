#!/usr/bin/env python3

# Script that puts torrent files in the proper folders using Torrent Tags
# so movie torrents would be put in the movies folder, ect.

# Author : Nolan Winsman
# Date : 2025-05-18


import qbittorrentapi # pip install qbittorrent-api

# documentation to API
# https://qbittorrent-api.readthedocs.io/en/latest/introduction.html


# dictionary to map torrent tags to folders
# the key is the torrent tag and the value is the folder it should be put in
def main():

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

    # retrieve all torrents and set their download folder to the corresponding tag
    for torrent in qbt_client.torrents_info():
        print(f'{torrent.name} ({torrent.state}) ({torrent.tags})')

if __name__ == "__main__":
    main()
