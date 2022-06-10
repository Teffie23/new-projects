import requests
from bs4 import BeautifulSoup
url='https://aphorism.ru/theme/welcome.html'
req=requests.get(url)
soup=BeautifulSoup(req.text,'lxml')
quotes=soup.find_all('font',class_='quote')
greeting_list=[]
for i in quotes:
    greeting_list.append(i.text)
greeting_list_update=('\n'.join(greeting_list).split('\n'))
greeting_list_update+=('\r'.join(greeting_list).split('\r'))
