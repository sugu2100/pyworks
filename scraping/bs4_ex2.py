from bs4 import BeautifulSoup

html_str = """
<html>
  <body>
    <ul class='item'>
        <li>인공지능</li>
        <li>빅데이터</li>
        <li>로봇공학</li>
    </ul>
    <ul class="lang">
        <li>Python</li>
        <li>Java</li>
        <li>C#</li>
    </ul>
  </body>
</html>
"""

soup = BeautifulSoup(html_str, 'html.parser')
first_ul = soup.find('ul', attrs={'class':'item'}) # attrs:속성을 의미 딕셔너리로 찾음
all_li = first_ul.find_all('li')  #find_all()는 찾은 값을 리스트로 반환
print(all_li)
print(all_li[1])
print(all_li[1].text)

