# Desktop Notifier - Python 🚀📰

Get live news headlines popping up on your desktop with this simple Python notifier!

First, download and install these dependencies: Python 3.7 or higher, requests, and plyer. in command prompt for window's
1. pip install requests
2. pip install plyer

Next, create a folder named desktop_notifier.
Inside that folder, create two files: 
1. topnews.py
2. notifier.py

Next, open "topnews.py" and paste this code inside. 👇



---



```python
import requests
import xml.etree.ElementTree as ET
import html
import re

RSS_FEED_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

def clean_text(text):
    if not text:
        return ""

    # Decode HTML entities
    text = html.unescape(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove source names after dash ( - BBC, - CNN, etc.)
    text = re.split(r"\s+-\s+", text)[0]

    # Remove non-readable junk characters
    text = re.sub(r"[^\x20-\x7E]", "", text)

    # Normalize spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

def loadRSS():
    return requests.get(RSS_FEED_URL, timeout=10).content

def parseXML(rss):
    root = ET.fromstring(rss)
    newsitems = []

    for item in root.findall("./channel/item"):
        title = clean_text(item.findtext("title", "No title"))

        # 🔑 Use title as message too (clean & reliable)
        newsitems.append({
            "title": title[:60],
            "description": title  # no messy RSS description
        })

    return newsitems

def topStories(limit=5):
    return parseXML(loadRSS())[:limit]


    return newsitems

def topStories(limit=5):
    return parseXML(loadRSS())[:limit]
```


#Next, open "notifier.py" and paste this code inside. 👇


```Python
import time
from plyer import notification
from topnews import topStories

APP_NAME = "News"  # VERY SHORT (critical)

def shorten(text, limit):
    if not text:
        return ""
    text = text.replace("\n", " ").strip()
    return text[:limit - 3] + "..." if len(text) > limit else text

newsitems = topStories(limit=5)

for news in newsitems:
    try:
        title = shorten(news["title"], 40)        # HARD SAFE LIMIT
        message = shorten(news["description"], 180)

        notification.notify(
            title=title,
            message=message,
            app_name=APP_NAME,
            timeout=10
        )

        time.sleep(15)

    except Exception as e:
        print("Notification skipped:", e)
```

Next, open VSCode, then open the terminal inside it.
Type this to navigate to your project folder:

1. cd desktop_notifier

Then run the notifier with:

2. python notifier.py


That’s it!
You’ll start seeing desktop notifications with the latest news headlines.
Enjoy staying updated without lifting a finger! 🚀📰


So just make sure you have the closing triple backticks before you start writing normal sentences!





