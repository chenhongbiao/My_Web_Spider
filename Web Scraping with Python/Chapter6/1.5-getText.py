from urllib.request import urlopen

#textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
#print(textPage.read())
print(str(textPage.read(), 'utf-8'))
#use str() method to decode it as "utf-8"
