import json
from steam.steamid import SteamID
user=SteamID.from_url('https://steamcommunity.com/id/Furnishings/')

from steam.webapi import WebAPI
api = WebAPI(key="45D432B97842C610AD4E38ABC4832B3B")

import requests as req
#from bs4 import BeautifulSoup

wishlist_url = "https://store.steampowered.com/wishlist/profiles/" + str(user) + "/wishlistdata/?p=0"

wishlist_page = req.get(wishlist_url)
wishlist_data = json.loads(wishlist_page.text)
with open("wishlist_file.json", "w") as write_file:
    json.dump(wishlist_data, write_file, separators=(",", ":"))

#print(wishlist_data)