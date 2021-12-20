import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)  #url 응답객체 생성
soup = BeautifulSoup(response.text, 'html.parser') #html 객체 생성
ul = soup.find('ul', attrs={'class':'data_lst'})
# print(ul)
li = ul.find('li')
# print(li)
exchange = li.find('span', attrs={'class':'blind'})  #환율 종류
print(exchange.text)
value = li.find('span', attrs={'class':'value'})     #환율 지수
print(value.text)
print(exchange.text, ':', value.text)
