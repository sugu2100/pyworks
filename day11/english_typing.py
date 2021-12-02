#영어 타자 게임
import random as r
import time

with open("word.txt", 'r') as f:
    word = f.readline().split()  # 단어 전체(공백문자로 구분)

n = 1   #문제 번호
input("[타자게임] 준비되면 엔터! ")
start = time.time()
while n < 11:
        print('-문제', n)
        question = r.choice(word)   #문제 단어 출제
        print(question)
        answer = input()                 #사용자가 답을 입력
        # 통과 아니면 오타 코드 작성
        if answer == question:
            print('통과!')
            n += 1        # 다음 문제 출제
        else:
            print("오타! 다시 도전!")

end = time.time()
print("게임 소요 시간 : %.2f초" % (end - start))