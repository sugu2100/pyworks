# 입력 받아 파일 쓰기

with open('input.txt', 'a') as f: #'a'모드는 추가
    text = input("저장할 내용을 입력해 주세요 : ")
    f.write(text)
    f.write('\n')
