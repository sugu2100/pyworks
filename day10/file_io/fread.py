# 파일 읽기

try:
    f = open("c:/web_dev/pyfile/season.txt", 'r')   #파일 읽기 모드 - 'r' 사용
    text = f.read()    # 파일 내용 전체 읽어옴(보조 기억장치)
    print(text)        # 콘솔에 출력(메모리)
    f.close()          # 파일 닫기
except:
    print("파일을 읽을 수 없습니다.")