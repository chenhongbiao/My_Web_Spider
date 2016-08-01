from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

#connection = pymysql.connect(host='localhost',
#                             user='root',
#                            db='mysql',
#                            charset='utf8mb4',
#                            cursorclass=pymysql.cursors.DictCursor)

conn = pymysql.connect(host="localhost",
                       user="root",
                       password="faustmeow",
                       db="mysql",
                       charset="utf8mb4")

cur = conn.cursor()
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

def store(title, content):
    #cur.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cur.execute("INSERT INTO pages (title, content) VALUES (%s, %s)", (title, content))
    cur.connection.commit()

#take an article link and store this link-page, then return a list of interal links that in this pages
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id":"mw-content-text"}).find("p").get_text()
    #take the first paragraph - use find
    store(title, content)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
#traverse randomly the wiki 
try:
    while len(links)>0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
