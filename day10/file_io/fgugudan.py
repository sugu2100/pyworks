# 구구단 파일 쓰기
# with ~ as 구문 -> f.close()를 사용하지 않음
with open('99.txt', 'a') as f:  #추가 쓰기 - 'a' 모드
    dan = 7
    for i in range(1, 10):
        times = "%d x %d = %d\n" % (dan, i, dan*i)
        f.write(times)
    f.write('\n')