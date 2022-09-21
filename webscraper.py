linkSet={}
from bs4 import BeautifulSoup
import requests
url=input("Enter the URL : ")
keyword=input("Enter keyword to be searched : ")
print("[+] Fetching links.....")
response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
for link in soup.find_all('a'):
    lin=link.get('href')
    if(lin.startswith('http')):
        linkSet[str(lin)]=requests.get(lin).status_code
for links in linkSet:
    if links.find(keyword) != -1:
        print(links," : ",linkSet[links])
print("Fetched Successfully...")
