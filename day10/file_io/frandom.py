# 파일 읽기
import random as r

f = open("c:/web_dev/pyfile/season.txt", 'r')   #파일 읽기 모드 - 'r' 사용

# 랜덤하게 자료 읽기
word = f.read().split()  #공백으로 구분
w = r.choice(word)
print(w)

f.close()          # 파일 닫기