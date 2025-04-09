#import feedparser
#import json
#import requests
#import os

#WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
#CACHE_FILE = "latest.json"

#ACCOUNTS = [
#    "BlueNoteTokyo",
#   "cottonclubjapan",
#    "billboardlive_t",
#    "billboardLive_y",
#    "billboardLive_o",
#    "LiveNationJapan",
#    "CMP_official",
#    "wmj_intl",
#]

#NITTER_BASE = "https://nitter.privacydev.net"

#if os.path.exists(CACHE_FILE):
#    with open(CACHE_FILE, "r") as f:
#        posted_ids = set(json.load(f))
#else:
#    posted_ids = set()

#new_posts = []

#for username in ACCOUNTS:
#    url = f"{NITTER_BASE}/{username}/rss"
#    feed = feedparser.parse(url)
#    for entry in feed.entries:
#        if entry.id not in posted_ids:
#            new_posts.append({
#                "id": entry.id,
#                "title": entry.title,
#                "link": entry.link,
#                "username": username
#            })
#            posted_ids.add(entry.id)

#for post in reversed(new_posts):
#    content = f"🆕 [{post['username']}] 新しい投稿:\n[{post['title']}]({post['link']})"
#    requests.post(WEBHOOK_URL, json={"content": content})

#with open(CACHE_FILE, "w") as f:
#    json.dump(list(posted_ids), f)

import feedparser
import requests
import os

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
ACCOUNTS = ["BlueNoteTokyo"]  # ←テスト用に1つだけに絞る

NITTER_BASE = "https://nitter.privacydev.net"

# 最新1件だけ通知する
for username in ACCOUNTS:
    url = f"{NITTER_BASE}/{username}/rss"
    feed = feedparser.parse(url)
    if feed.entries:
        entry = feed.entries[0]
        content = f"🧪 通知テスト：[{username}] 最新投稿\n[{entry.title}]({entry.link})"
        print("Sending:", content)
        requests.post(WEBHOOK_URL, json={"content": content})
