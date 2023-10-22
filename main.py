import json
from steam.steamid import SteamID
user=SteamID.from_url('https://steamcommunity.com/id/Furnishings/')

from steam.webapi import WebAPI
api = WebAPI(key="45D432B97842C610AD4E38ABC4832B3B")

import requests as req

wishlist_url = "https://store.steampowered.com/wishlist/profiles/" + str(user) + "/wishlistdata/?p=0"

wishlist_page = req.get(wishlist_url)
wishlist_data = json.loads(wishlist_page.text)
with open("wishlist_file.json", "w") as write_file:
    json.dump(wishlist_data, write_file, separators=(",", ":"), indent=10)

current_sales = {}
for titleid,attributes in wishlist_data.items(): #create nested loop to interact with further dict levels
    if str(attributes).find('"discount_pct":null') == False:
        current_sales[titleid]=attributes

print(current_sales.keys())