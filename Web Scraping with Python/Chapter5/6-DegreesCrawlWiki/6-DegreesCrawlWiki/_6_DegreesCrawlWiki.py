from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql

#CREATE TABLE pages (id  INT NOT NULL AUTO_INCREMENT,
                   #url VARCHAR(255) NOT NULL,
                   #created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                   #PRIMARY KEY (id));

#CREATE TABLE links (id  INT NOT NULL AUTO_INCREMENT,
                   #fromPageId INT NULL,
                   #toPageId INT NULL,
                   #created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                   #PRIMARY KEY (id));

#
#identify a link by saying, ¡°There exists a link on page A, which connects to page B.
#That is, INSERT INTO links (fromPageId, toPageId) VALUES (A, B); (where ¡°A¡± and
#¡°B¡± are the unique IDs for the two pages)
#

# Connect to the database
conn = pymysql.connect(host='localhost',
                             user='root',
                             password='faustmeow',
                             db='mysql',
                             charset='utf8mb4')

cur = conn.cursor()
cur.execute("USE scraping")

def pageScraped(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()
    #print(page) - page as a Python dict object?
    #print(page[0]) - 
    cur.execute("SELECT * FROM links WHERE fromPageId = %s", (int(page[0])))
    #False - We have encountered a new page, add it and search it for links
    #this url didn't use as a fromPage
    if cur.rowcount == 0:
        return False
    return True

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (%s)", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)) )
    if cur.rowcount == 0 :
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)", (int(fromPageId), int(toPageId)))
        conn.commit()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    #hit the six point, return
    #get the pageId and if it's new page, insert it and return its id
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    #for all internal article links of this page,  
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        #build the link relationship in links table
        if not pageScraped(link.attrs['href']):
            #False - We have encountered a new page, add it and search it for links
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel+1)
        else: 
            print("Skipping: "+str(link.attrs['href'])+" found on "+pageUrl)

getLinks("/wiki/Kevin_Bacon", 0) 
cur.close()
conn.close()