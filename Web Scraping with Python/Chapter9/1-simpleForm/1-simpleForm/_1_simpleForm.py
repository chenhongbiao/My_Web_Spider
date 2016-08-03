import requests
params = {"firstname":"cat", "lastname":"faust"} 
#r = requests.post("http://pythonscraping.com/pages/files/form.html",data=params)
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r)
print(r.text) #yeah, requests.post() response, using .text

#params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
#r = requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi", data=params)
#print(r.text)

#params = {"email_addr":"faustmeow@163.com"}
#r = requests.post("https://conduit.ipost.com/forms.cgi", data = params)
#print(r.text)
#<form action="https://conduit.ipost.com/forms.cgi" method="post" id="newsletter-subscribe">
