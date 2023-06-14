import requests
from bs4 import BeautifulSoup

url = input(" enter full URL : ")
file_name= input("Enter File name to store links : ")
file = open(file_name,"w")

links=[]

def crawler(url):
    website = requests.get(url)
    web_parse = website.text
    soup= BeautifulSoup(web_parse,"lxml")

    for link in soup.findAll('a'):
       links.append(link.get('href'))
    for link in links:
        file.write(str(link))
        file.write("\n")

crawler(url)
