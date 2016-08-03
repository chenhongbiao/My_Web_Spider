import requests

#open() - open a flie and return a stream
files = {"uploadFile": open("H:\SpiderPic\sci_hub-TE.jpg","rb")}
#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
#It defaults to 'r' which means open for reading in text mode.
#In text mode, if encoding is not specified the encoding used is platform dependent
#The default mode is 'r' (open for reading text, synonym of 'rt'). 

#For binary read-write access, the mode 'w+b' opens and truncates the file to 0 bytes. 
#'r+b' opens the file without truncation. #'r'	open for reading; 'b'	binary mode

r = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)
#<input type="file" name="uploadFile">
print(r.text)