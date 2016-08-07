import requests
import re
import lxml
import urllib
from lxml import etree

youtubeURL = "https://youtu.be/DUFjNiusLEw"
youtubeID = re.findall('watch\?v=(.+)', youtubeURL)

if len(youtubeID) == 0:
    youtubeID = re.findall('\..+?\/(.+)', youtubeURL)

youtubeID = youtubeID[0]
print(youtubeID)

youtube = etree.HTML(urllib.urlopen(youtubeURL).read())
video_title = youtube.xpath("//span[@id='eow-title']/@title")
video_title = ''.join(video_title)

url = "http://yt2fb.com/wp-admin/admin-ajax.php"

querystring = {"action":"create_youtube_link","title":video_title,"description":"","starttimesec":"0","attach_id":"","playback":"Facebook","youtubeID":youtubeID}

headers = {
    'accept': "*/*",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    'dnt': "1",
    'referer': "http://yt2fb.com/",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "en-US,en;q=0.8",
    'cookie': "__cfduid=d83bfe9370be40ef2691bee16d92e5aa11470445368; _ga=GA1.2.846252117.1470445371; _gat=1; __cfduid=d83bfe9370be40ef2691bee16d92e5aa11470445368; _gat=1; _ga=GA1.2.846252117.1470445371",
    'cache-control': "no-cache",
    'postman-token': "6c099f20-a8b9-777f-0fc6-d7ab060c4be1"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)