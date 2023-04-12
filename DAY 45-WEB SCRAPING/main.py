#html dosyasını buradan açalım
from bs4 import BeautifulSoup

with open("website.html",encoding="utf8") as file:
    content=file.read()

soup=BeautifulSoup(content,"html.parser")
print(soup) 
'''dilersek tüm kodu görüntüleyebiliriz.'''

print(soup.title) #başlığı verir

print(soup.title.name)#title başlığı verir

print(soup.title.string) #title içindeki değeri verir

print(soup.prettify()) #girintili hale getirerek daha okunaklı html kodu elde edilir.

print(soup.a) #sitede bulunan ilk anchor tagı verir.

print(soup.p) #sitede bulunan ilk paragrafı  verir.

print(soup.li) #sitede bulunan ilk liste tagını verir.

print("--------------------------------------------------------------")
######

#ilk örneklerde sadece ilk değerin p - li- yada a gibi tagları aldık diğerlerine erişemedik. peki hepsine erişmek istesek.

all_anchor_tag_li=soup.find_all(name="li") #içine girilen değerin veya tagın kapsadığı tüm değerleri getirir.
print(all_anchor_tag_li)

#pekii.. sadece içindeki str değerleri yazdırmak istersek
for tag in all_anchor_tag_li:
    print(tag.getText())
print("--------------------------------------------------------------")

# liste içindeki metni aldık peki link değeri içeren metindeki linkleri almak istesek.
#onun öncesinde link içeren tagın metin değeri alalım
all_anchor_tag_a=soup.find_all(name="a") 
for i in all_anchor_tag_a:
    #print(i.getText())
    print(i.get("href")) # sadece link değerini verir.

print("--------------------------------------------------------------")

#arama yapmak istediğim bir değerin çok fazla value değerleri var ise h-p a vb gibi. 
# #onun yerine id veya classname gibi özel adlarla sınırlandırılabilir.

heading=soup.find_all("h1", id="name") #id name olan değerleri gösterir
#print(heading)

section_heading=soup.find_all(name="h3",class_="heading")
print(section_heading)

for i in section_heading: #isimlerini öğrenmek istiyorsak 
    a=i.getText()
    print(a)

print("--------------------------------------------------------------")

#istediğimiz bir bağlantının linkini almak istersek

url=soup.select_one(selector="p a") #p tagın içindeki a tagını alır
print("url tagı:",url) 

#sadece url için de kullanmayabiliriz.
name=soup.select_one(selector="#name")
print("name tagı:",name)

print("--------------------------------------------------------------")


#başlık sınıfına ait tüm değerleri çekmek istiyorsak
head=soup.select(selector=".heading")
print(head)