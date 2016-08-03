from selenium import webdriver
from bs4 import BeautifulSoup
import time

#don't trick by the path like: D:\Internet-IE\phantomjs-2.1.1-windows\bin - repalce '\' to '/'
driver = webdriver.PhantomJS(executable_path="D:/Internet-IE/phantomjs-2.1.1-windows/bin/phantomjs")
#and you need to add phantomjs.exe path in your system OS PATH and you can test it in your cmd: phantomjs
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html") # driver load the page and wait...
#time.sleep(1)
time.sleep(3)
#print(driver)
#print(driver.find_element_by_id("content").text)
pageSource = driver.page_source #get the source of the current page
bsObj = BeautifulSoup(pageSource,"html.parser")
print(bsObj.find(id="content").get_text())
driver.close()

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.PhantomJS(executable_path="D:/Internet-IE/phantomjs-2.1.1-windows/bin/phantomjs")
#driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")

#try:
    #element = WebDriverWait(driver=driver,timeout=10).until(EC.presence_of_all_elements_located( (By.ID, "loadedButton") ))
    #print(element)
#finally:
    #print(driver.find_element_by_id("content").text)
    #driver.close()

