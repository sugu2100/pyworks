import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)  #url 응답객체 생성
soup = BeautifulSoup(response.text, 'html.parser') #html 객체 생성
ul = soup.find('ul', attrs={'class':'data_lst'})
# print(lis)
# 전체 환율 찾기
lis = ul.find_all('li')
for li in lis:
    exchange = li.find('span', attrs={'class':'blind'})  #환율 종류
    value = li.find('span', attrs={'class':'value'})     #환율 지수
    # print(exchange.text, ':', value.text)
    print(exchange.string.split(' ')[-1], ':', value.text)
    #공백문자로 구분(split함수)해서 맨 뒤의 문자열 추출
