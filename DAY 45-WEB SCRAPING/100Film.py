from bs4 import BeautifulSoup
import requests
filmler=[]
new_film=[]
url=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
page=url.text

soup=BeautifulSoup(page,"html.parser")

film_numb=soup.find_all(name="h3",class_="title")

for i in film_numb:
    filmler.append(i.get_text())

print("-----------------------------")
# print(filmler)
new=filmler[::-1]

print("-----------------------------")

with open("filmler.txt","w",encoding="utf-8") as f:
    for i in new:
        f.write(i+"\n")