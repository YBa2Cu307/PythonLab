import requests
from bs4 import BeautifulSoup
import json

strona= requests.get('https://www.twostepsfromhell.com/')
#print(strona.status_code)
zupa=BeautifulSoup(strona.text,'html.parser')
albumy=zupa.find("div",{'class': 'isotope-wrapper px-gutter'})
al=albumy.find_all("a")
al2=[]
al3=[]

for i in range(len(al)):
    al2.append(str(al[i]))
    al2[i]=al2[i].split("/")
    al3.append(al2[i][5])
    print(al2[i][5])
with open('abc.json','w') as f:
    json.dump(al3,f)