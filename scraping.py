#C:\Users\dhava\AppData\Local\Programs\Python\Python37-32\Scripts
#^^for personal reminders lol
import requests
from bs4 import BeautifulSoup

print("----------------------------")
print("-------Lyric Finder!--------")
print("----------------------------")
while True:
    artistName = input("Pick an artist whose lyrics you'd like to search! ")
    spacesInArtistName = 0
    for i in range(len(artistName)):
        if(artistName[i] == " "):
            spacesInArtistName+=1
    if " " in artistName:
        artistName = artistName.replace(" ", "-", spacesInArtistName)
    artistName = artistName + "-"

    songName = input("Pick a song by them! ")
    spacesInSongName = 0
    for j in range(len(songName)):
        if(songName[j] == " "):
            spacesInSongName+=1
    if " " in songName:
        songName = songName.replace(" ", "-", spacesInSongName)

    urlPrefix = 'https://genius.com/' + artistName
    #thanks genius^
    urlSuffix = '-lyrics'

    finalURL = urlPrefix + songName + urlSuffix
    response = requests.get(finalURL)
    if response.status_code == 404:
        print("Error: song or artist not found!")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find(class_='lyrics')
        print(element.get_text())
    x = input("Would you like to repeat the program? (Y or N) ")
    if x == "N" :
        break

