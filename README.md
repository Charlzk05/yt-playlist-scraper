## yt playlist scraper
A YouTube playlist scraper. Requires Python 3.11+ and pytube to work
This script will download the video of every contents in a YouTube playlist.

[check out yt playlist mp4 downloader](https://github.com/Charlzk05/yt-playlist-mp4)

### Packages and versions
- pytube==12.1.0

### Installation
1. git clone ``https://github.com/Charlzk05/yt-playlist-scraper.git`` or download the source code
2. navigate to the folder
3. do ``pip install -r requirements.txt`` to install the package from requirements.txt
4. do ``py main.py``
5. enjoy!

### Usage
- Please enter the url of the playlist you wish to scrape: - playlist from youtube only
  - e.g. https://www.youtube.com/playlist?list=OLAK5uy_kOhxZJmu14hn8tCliKIFz6-p6D4YKOV3g
- ``Scrapes destination (optional):`` - must insert the full path
  - e.g. C:\Users\Username\Folder

### Json result
```json
{
    "Video": {
        "Title": yt.title,
        "ID": yt.video_id,
        "Length": str(yt.length) + " secs",
        "Description": yt.description,
        "Stats": {
            "Views": yt.views
        }
    },
    "Channel": {
        "Url": yt.channel_url,
        "ID": yt.channel_id
    }
}
```
