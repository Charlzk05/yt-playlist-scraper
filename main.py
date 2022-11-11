import os, json
from pytube import Playlist, YouTube

def run(pl):
    # insert the Scrapes destination (optional)
    # e.g. C:\Users\Username\Folder
    filepath = input("Scrapes destination (optional): ")
    
    links = pl.video_urls
    
    for l in links:
        os.system("cls")
        yt = YouTube(l)
        
        content = yt.streams.first()
        print(f"{content.default_filename.replace('.3gpp', '')} Scraping ...")
        
        result = {
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
        
        json_object = json.dumps(result, indent=4)
        
        if filepath == "":
            if os.path.exists("./Scrapes"):
                with open(os.path.join("./Scrapes", f"{content.default_filename[0:-5].replace(' ', '')}.json"), "w") as output:
                    output.write(json_object)
            else:
                os.mkdir("./Scrapes")
                with open(os.path.join("./Scrapes", f"{content.default_filename[0:-5].replace(' ', '')}.json"), "w") as output:
                    output.write(json_object)
        else:
            with open(os.path.join(filepath, f"{content.default_filename[0:-5].replace(' ', '')}.json"), "w") as output:
                    output.write(json_object)
                    
        print(content.default_filename[0:-5] + " Done!")

if __name__ == "__main__":
    url = input("Please enter the url of the playlist you wish to scrape: ")
    pl = Playlist(url)
    run(pl)