import os
import urllib.request
from bs4 import BeautifulSoup as BS 
import requests

print("Your current path: " + os.getcwd())
new_path = input("Enter Your New Path")
os.chdir(new_path)
l = int(input('first comic index( >= 39)'))
h = int(input('last comic index( <= 4537)'))
for i in range(l, h+1):
	url = 'http://explosm.net/comics/' + str(i)
	src_code = requests.get(url)
	code = src_code.text
	soup = BS(code, 'html.parser')
	for img in soup.find_all('img', {'id':'main-comic'}):
		img_url = 'http:' + img.get('src')
		print(img_url)
		img_url = img_url.strip()
		urllib.request.urlretrieve(img_url, 'Comic' + str(i) + '.jpeg')
