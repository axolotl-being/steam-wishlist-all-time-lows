import json

from steam.steamid import SteamID
user=SteamID.from_url('https://steamcommunity.com/id/Furnishings`d/')

from steam.webapi import WebAPI
api = WebAPI(key="") #insert personal API key here

import requests as req

wishlist_url = "https://store.steampowered.com/wishlist/profiles/" + str(user) + "/wishlistdata/?p=0"

wishlist_page = req.get(wishlist_url)
wishlist_data = json.loads(wishlist_page.text)
with open("wishlist_file.json", "w") as write_file:
    json.dump(wishlist_data, write_file, separators=(",", ":"), indent=10)

"""
with open('wishlist_file.json') as user_file:
    file_contents = user_file.read()

wishlist_data = json.loads(file_contents)
"""
current_sales = {}
for titleid,attributes in wishlist_data.items(): 
    if wishlist_data[titleid]['subs']: #need to check for nonempty since some games have not released yet and don't have data populated
    
        if wishlist_data[titleid]['subs'][0]['discount_pct'] != None:
            current_sales[titleid] = attributes
    
for titleid,attributes in current_sales.items():
    print(current_sales[titleid]['name']) #we now have a list of all games that are on sale right now!


#steamdb.info doesn't allow scraping and there are no other up to date sites, so without creating my own database, I cannot finish this project RIP
"""
from requests import get as req
from bs4 import BeautifulSoup
def price_scraper(titleid):
    url="https://steampricehistory.com/app/" + str(titleid) 
    results = req.get(url)
    soup = BeautifulSoup(results.text, "html.parser")
    table=soup.find('table', class_='table table-fixed table-prices table-hover table-sortable')

"""