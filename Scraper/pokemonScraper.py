import requests
import shutil
from bs4 import BeautifulSoup

def downloadImage(url, fileName):
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(url, stream = True)
    # Check if the image was retrieved successfully
    if r.status_code == 200:
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
    # Open a local file with wb ( write binary ) permission.
        with open(fileName,'wb') as f:
            shutil.copyfileobj(r.raw, f)    
        print('Image sucessfully Downloaded: ',fileName)
    else:
        print('Image Couldn\'t be retreived')


url = "https://pokemondb.net/sprites"
#let's get html from the page
page_response = requests.get(url,timeout = 5)
content = BeautifulSoup(page_response.text,"html.parser")

pokeData = []
#we use find when we just want one element
pokeMainTitle = content.find('h1')
pokeTitle = content.find(id='gen1')
print(pokeMainTitle.text)
print(pokeTitle)
#we can also avoid sending attrs and it will get all the <a>
pokeLinks = content.find_all("a",attrs= {"class":"infocard"})

for poke in pokeLinks:
    #we can get the tag attributes like if it is an dictionary we can also use .get('href')
    pokeNameRoute = poke['href'].split("/")[2]
    print(pokeNameRoute)
    pokeUrl = url + "/"+pokeNameRoute
    print(pokeUrl)
    pokeDetail = requests.get(pokeUrl,timeout = 5)
    pokeContent = BeautifulSoup(pokeDetail.text,"html.parser")
    pokeImages = pokeContent.find_all("img",attrs= {"class":"img-sprite-v11"})
    for image in pokeImages:
        src = image['src']
        print(src)
        #let's see if the pokemon is shiny o normal
        urlSplit = src.split('/')
        type = urlSplit[5]
        imgName=urlSplit[-1]
        print(type)
        if(type == "normal"):
            downloadImage(src,imgName)
        elif (type == "shiny"):
            downloadImage(src,"shiny_"+urlSplit[-1])
        elif (type == "back-shiny"):
            downloadImage(src,"shiny_back_"+urlSplit[-1])
        elif (type == "back-normal"):
            downloadImage(src,"_back_normal"+urlSplit[-1])
