# 1부터 n까지 곱하기
def facto(n):
    gob = 1
    for i in range(1, n+1):
        gob *= i
    return gob

print(facto(1))   #1 1 x 1
print(facto(2))   #2 1 x 2
print(facto(2))   #6 1 x 2 x 3
