#The HTTP API takes GET requests in the following schema:
#freegeoip.net/{format}/{IP_or_hostname}
#Supported formats are: csv, xml, json and jsonp. 
#If no IP or hostname is provided, then your own IP is looked up.
from urllib.request import urlopen
import json

ojson = urlopen("https://freegeoip.net/json/github.com")
print(ojson)
print(ojson.read())

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode("utf-8")
    #want to decode the bytes which use the "xx" encoding method
    responseJson = json.loads(response)
    #return responseJson.get("country_name")
    return responseJson["country_name"]
    #in Python dict you can use method .get() or just responseJson["country_name"]

print(getCountry("github.com"))
print(getCountry("50.78.253.58"))

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}], "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"}, {"fruit":"pear"}]}'
jsobj = json.loads(jsonString)

print(jsobj.get("arrayOfNums"))
print(jsobj["arrayOfNums"][1])
print(jsobj.get("arrayOfFruits")[2]["fruit"])
print(jsobj.get("arrayOfFruits")[2].get("fruit"))