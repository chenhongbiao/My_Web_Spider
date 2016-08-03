import requests

params = {"username":"anything", "password":"password"}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)
print(r.headers)
print("Cookie is set to: ")
print(r.cookies.get_dict())
print("---------------------")
print("Let's use cookie to go to profile page")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies= r.cookies)
print(r.text)

#session = requests.Session()
#s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)

#print(s.headers)
#print("Cookie is set to: ")
#print(s.cookies.get_dict())
#print("---------------------")
#print("Let's use cookie to go to the profile page:")
#s = session.get("http://pythonscraping.com/pages/cookies/profile.php",cookies=s.cookies)
#print(s.text)