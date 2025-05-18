# qbittorrent-cleanup

---

Script that deletes qbittorrent torrents that are older than 90 days.

WARNING: This also deletes the files. Please understand how the script works and what it does before running it.

## Disclaimer

This script uses the qbittorrent-api to interface with qBittorrent. It is intended for legal and ethical uses only, and I do not promote or condone piracy or illegal downloading.

Please use this script responsibly and only for its intended purposes. Any illegal or unethical use of this script is strictly prohibited and not supported by the author.

## Installation

1. Clone the repo

```sh
git clone https://github.com/nolanwinsman/qbittorrent-cleanup.git
```

# Setting Up a Python Virtual Environment

2. **Navigate to your project directory:**

```sh
cd /path/to/your/project
```

3. Create a virtual environment

```sh
python3 -m venv .venv
```

4. Activate the virtual environment

```sh
source .venv/bin/activate
```

5. Install dependencies

```sh
pip install -r requirements.txt
```

## Setup

Script requires a few changes before use. The default credentials for the Qbittorrent web-ui are used for this script. If you use different credentials, you will need to change it in both files.

```py
    qbt_client = qbittorrentapi.Client(
        host='localhost',
        port=8080,
        username='admin',
        password='adminadmin'
    )
```

## Contact

Nolan Winsman - [@Github](https://github.com/nolanwinsman) - nolanwinsman@gmail.com

Project Link: [https://github.com/nolanwinsman/qbittorrent-cleanup](https://github.com/nolanwinsman/qbittorrent-cleanup)

## Contributers

- nolanwinsman
