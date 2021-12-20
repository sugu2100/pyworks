import requests
from bs4 import BeautifulSoup

def getcontent(): #주식 종목 html 내용 가져오기 함수
    url = "https://finance.naver.com/item/main.naver?code=005930"
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

content = getcontent()  #호출
today = content.find('div', attrs={'class':'today'})
# print(today)
price = today.find('span', attrs={'class':'blind'})
print(price)
print("삼성전자 주가 : {}원".format(price.text))