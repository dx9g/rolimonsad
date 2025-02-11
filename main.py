import json
import random
import time
import requests
from rich import print

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

session = requests.Session()
session.cookies.update({"_RoliVerification": config.get("roli_verification")})

player_id = config.get("player_id")

# Manually input limited item IDs you want to offer
offer_items = [
    
]

# Manually input limited item IDs you want to request (leave empty if not specific)
request_items = [
    
]

# Manually input request tags (e.g., "any", "downgrade")
request_tags = []

def post_ad(item_ids: list[int], request_ids: list[int], tags: list[str]) -> None:
    combined_tags = tags if tags else []
    
    req = session.post("https://api.rolimons.com/tradeads/v1/createad", json={
        "player_id": player_id,
        "offer_item_ids": item_ids,
        "request_item_ids": request_ids,
        "request_tags": combined_tags
    })

    res = req.json()
    if res.get("success", None):
        print(f"[bold green]SUCCESS[/] Ad posted {item_ids} - Requested: {request_ids if request_ids else 'None'} - Tags: {combined_tags}")
        return

    print(f'[bold red]ERROR[/] Couldn\'t post ad (Reason: {res.get("message")})')

while True:
    post_ad(offer_items, request_items, request_tags)

    random_time = random.randint(15, 15)
    print(f"Waiting {random_time} minutes before attempting to post another ad")
    time.sleep(random_time * 60)
