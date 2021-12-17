import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)  #url 응답객체 생성
soup = BeautifulSoup(response.text, 'html.parser') #html 객체 생성
# ul = soup.find('ul', attrs={'class':'data_lst'})
li = soup.select_one('ul.data_lst li') #태그이름.클래스이름
print(li)
#print(ul)
#li = ul.find('li')
# print(li)
exchange = li.select_one('span.blind')
#print(exchange.text)
value = li.select_one('span.value')
#print(value.text)
print(exchange.text, ':', value.text)
