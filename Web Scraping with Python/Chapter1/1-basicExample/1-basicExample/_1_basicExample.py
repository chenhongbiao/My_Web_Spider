
from urllib.request import urlopen
# only import a function urlopen
# if you use python 2.x you will use urllib2
# in python 3.x, urllib2 was renamed as urllib and was spilt into three submodules
# they are urllib.request , urllib.parse, and urllib.error

url = "http://chenhongbiao.github.com"
html = urlopen(url)
print(html)
#html is a http Resopnse object = -=
# the function urlopen can open and ... read a remote object
print(html.read())

#notice that Chinese would not show in the terminal in decode
#it would show the raw code