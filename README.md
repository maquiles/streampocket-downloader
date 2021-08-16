# STREAMPOCKET DOWNLOADER

Download audio files from soundcloud or youtube links using streampocket.com for conversions.

## Install Requirements
```
git
python 3
pip
requests
```

## Prerequisites
* clone the repo
```
git clone TODO
```
* install requests package
```
pip install requests
```

## Usage
* Can run for single link or from textfile of links.
* To run for single link, use url as argument to script.
* To run from list of links in textfile, first create a textfile of links, and then pass the file as an argument to the script. (Easiest to make textfile in same directory as download.py file)
* Files download to a new directory called /audio that will be created.

```
# for single link
python3 download.py -l LINK
python3 download.py --link LINK
# e.g.
python3 download.py -l https://soundcloud.com/sumthinsumthin/vivid-1

# for textfile of links
python3 download.py -f FILENAME
python3 download.py --file FILENAME
# e.g. for list of URLs in text file called dl_links.txt in same directory as download.py
python3 download.py -f dl_links.txt
```

