from urllib.request import urlopen

#textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
#print(textPage)
print(str(textPage.read()),"utf-8")

#from urllib.request import urlopen
#from bs4 import BeautifulSoup

#html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
#bsObj = BeautifulSoup(html,"html.parser")
#content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
#content = bytes(content, "UTF-8")
#content = content.decode("UTF-8")
#print(content)
#print(bsObj) #'gbk' codec can't encode character '\xa0' in position 9173: illegal multibyte sequence
                         #because this terminal is presenting character as gbk decode
#print(bsObj.get_text())
