import requests
from bs4 import BeautifulSoup
url='https://веселун.рф/anekdoty/shutki'
re=requests.get(url)
soup=BeautifulSoup(re.text,'lxml')
quotes=soup.find_all('article',class_='intem')

list_of_jokes=[]
for i in quotes:
    list_of_jokes.append(i.p.text)
