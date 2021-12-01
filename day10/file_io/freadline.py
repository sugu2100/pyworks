# 파일 읽기
import random as r

f = open("c:/web_dev/pyfile/season.txt", 'r')   #파일 읽기 모드 - 'r' 사용
#season = f.readline()   #한 줄(첫줄) 읽기
#print(season)
seasons = f.readlines()  #전체 라인 읽기, 리스트로 반환해서 저장
print(seasons)
# print(seasons[0])
# print(seasons[-1])

# 전체 읽기
for season in seasons:
    #print(season)
    print(season.strip()) #한줄 공백 제거

f.close()          # 파일 닫기