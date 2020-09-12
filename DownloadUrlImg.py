from bs4 import BeautifulSoup
import urllib.request
import requests
import os
os.system("cls")

COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

print(colorText("[[blue]]SCRIPT [[yellow]]made [[red]]by [[blue]]Dra[[yellow]]gos[[red]]hell"))
print("")
 

# setting URL destination
valid=False

while True:
    url = input(colorText("[[white]]Enter the full path of the url:"))
    try:
        response = requests.get(url)
        print(colorText("[[green]]URL valid"))
        break
    except Exception as e:
        print(colorText("[[red]]Invalid URL please try again"))



# retrieving HTML payload from the website
response = requests.get(url)

# checking response.status_code (if you get 502, try rerunning the code)
if response.status_code != 200:
    print(f"Status: {response.status_code} — Try rerunning the code\n")
else:
    print(f"Status: {response.status_code}\n")

# using BeautifulSoup to parse the response object
soup = BeautifulSoup(response.content, "html.parser")

# finding Post images in the soup
# images = soup.find_all("img", attrs = {"alt": "Post image"}) --> for attributes
images = soup.find_all("img")



# downloading images
number = 0
for image in images:
    print(colorText("[[green]](IMG_nr."+str(number)+")---->IMG_path: "+image["src"]))
    image_src = image["src"]
    urllib.request.urlretrieve(image_src, "img"+str(number)+".jpg")
    #urllib.request.urlretrieve(image_src, "img"+str(number)+".png")    
    #urllib.request.urlretrieve(image_src, "img"+str(number))
    number += 1
print(colorText("[[yellow]]---------------------------------------------"))
print("Total number of images downloaded:"+str(number))
print("---------------------------------------------")
print("Thanks for using my script")
print("---------------------------------------------")
x=input("Press any key to exit")