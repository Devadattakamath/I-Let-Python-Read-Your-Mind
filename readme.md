python desktop notifier 

Make sure Python is installed, then install the required packages: 

1. pip install requests
2. pip install plyer

After installing the required packages, create a folder named "desktop_notifier" 
inside it create two files: 

1. topnews.py
2. notifier.py

Now, open "topnews.py" and paste the following code into it. 👇 

```Python
import requests
import xml.etree.ElementTree as ET
import html
import re

RSS_FEED_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

def clean_text(text):
    if not text:
        return ""

    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"http\S+", "", text)
    text = re.split(r"\s+-\s+", text)[0]
    text = re.sub(r"[^ -~]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
    
def loadRSS():
    return requests.get(RSS_FEED_URL, timeout=10).content

def parseXML(rss):
    root = ET.fromstring(rss)
    newsitems = []
    
    for item in root.findall("./channel/item"):
        title = clean_text(item.findtext("title", "No title"))

        newsitems.append({
            "title": title[:60],
            "description": title  # no messy RSS description
        })
    

    return newsitems

def topStories(limit=5):
    return parseXML(loadRSS())[:limit]
   
```

Next, open "notifier.py" and paste the code below into it. 👇 

```python
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

Steps to run your program in VS Code’s command prompt: 

1. Navigate to the project folder by typing: 

   cd desktop_notifier  

3. Run the Python script with:

   python notifier.py

“And that’s it — our notifier is working! 🎉”













