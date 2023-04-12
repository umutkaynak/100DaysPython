from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com/newest") #gider
print(response.text)#html texti görüntüleyelim
print("--------------------------------------------------------------------------------------------------------------------------------------------")

#yapmak istenen başlıkları ve bağlantıları çekmek
yc_web_page=response.text

soup= BeautifulSoup(yc_web_page,"html.parser") 
#print(soup.title)#title erişmek için

article_tag=soup.find(name="a",rel="nofollow")
article_text=article_tag.get_text()

article_link=article_tag.get("href")

article_upvode=soup.find(id ="score_35529844")

print(article_text)
print(article_link)
print(article_upvode.get_text())


print("--------------------------------------------------------------------------------------------------------------------------------------------")

text=[]
link=[]
article_tags=soup.find_all(name="a",rel="nofollow")

for article_tag in article_tags:
    article_texts=article_tag.get_text()
    text.append(article_texts)
    article_links=article_tag.get("href")
    link.append(article_links)

article_upvodes=[i.get_text() for i in soup.find_all(name="span", class_ ="score")]
# print(article_texts)
# print(article_links)
# print(article_upvodes.get_text())
print(text[:])
print(link[:])
print(article_upvodes)

print("--------------------------------------------------------------------------------------------------------------------------------------------")
#şimdi score değerlerini sadece int şeklinde yazalım

print(article_upvodes)
print(article_upvodes[0].split()[0]) 
#peki bunu tüm listeye uyarlayalım
print("--------------------------------------------------------------------------------------------------------------------------------------------")

new_article_upvodes=[int(i.get_text().split()[0]) for i in soup.find_all(name="span", class_ ="score")]
print(new_article_upvodes)

print("--------------------------------------------------------------------------------------------------------------------------------------------")
#şimdi en yüksek bağlantısı yani skor olanı alıp karşılık gelen text değerlerini almak istersek nasıl yapılmalı

max_number=max(new_article_upvodes) # en yüksek skora sahip değer
print(max_number)

largest_number=new_article_upvodes.index(max_number)
print(largest_number)
text_index=text[largest_number]
link_index=link[largest_number]

print(text_index)
print(link_index)
