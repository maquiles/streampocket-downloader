import os
import sys
import urllib.parse as link_parser
import urllib.request
import requests


streampocket_link = "http://streampocket.net/json2?stream="
audio_dir = "audio/"

def get_file_from_streampocket(link):
  safe_link = link_parser.quote_plus(link)
  streampocket_request_url = streampocket_link + safe_link
  streampocket_response = requests.get(streampocket_request_url)
  if streampocket_response.text == "":
    print("ERROR - " + link)
    return
  response_json = streampocket_response.json()
  file_url = response_json["recorded"]  
  file_name = response_json["filename"]
  print("DOWNLOADING - " + file_name)
  download_response = requests.get(file_url)
  with open(audio_dir + file_name, "wb") as file:
    file.write(download_response.content)
  print("COMPLETE - " + file_name)


def bulk_download_from_textfile(file_name):
  with open(file_name, "r") as file:
    for line in file:
      url_string = str(line)
      get_file_from_streampocket(url_string.strip())


if __name__ == "__main__":
  os.mkdir(audio_dir)
  tag = sys.argv[1]

  if tag == "-h" or tag == "--help":
    print("The script will download an audio file from soundcloud or youtube to the directory the script is in.")
    print("The script uses streampocket.com to get the audio file.\n")
    print("-h --help            :  You're looking at it.")
    print("-l --link [LINK]     :  Download from a single link.")
    print("-f --file [FILENAME] :  Bulk download from a text file of link(s).")
  elif tag == "-l" or tag == "--link":
    print("Downloading from link...\n")
    try:
      link = sys.argv[2]
      get_file_from_streampocket(link)
    except IndexError:
      print("ERROR - No link argument found")
  elif tag == "-f" or tag == "--file":
    print("Bulk downloading from text file...\n")
    try:
      filename = sys.argv[2]
      bulk_download_from_textfile(sys.argv[2])
    except IndexError:
      print("ERROR - No filename argument found")
  else:
    print("Incorrect argument. Use -h for help with usage.\n")

