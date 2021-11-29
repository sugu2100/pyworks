# 거북이 대포 게임
# 각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임
import turtle as t
import random as r

# 좌표 이동
"""
t.up()
#좌표 이동 함수 - t.goto(x, y)
t.goto(0, 200)  #x좌표: 0, y좌표 : 200
t.goto(0, -200)  #x좌표: 0, y좌표 : -200
t.goto(200, 0)  #x좌표: 200, y좌표 : 0
t.goto(-200, 0)  #x좌표: -200, y좌표 : 0
"""
def turn_up():  #위쪽 화살키를 누르면
    t.left(2)   #거북이를 왼쪽으로 2도 돌림

def turn_down():  #아래쪽 화살키를 누르면
    t.right(2)   #거북이를 오른쪽으로 2도 돌림

def fire():
    ang = t.heading()  #거북이가 바라보는 각도 저장

    while t.ycor() > 0: # 거북이의 y좌표가 0보다 크면(땅위에 있는 동안)
        t.forward(15) # 15픽셀 이동
        t.right(5)    # 오른쪽으로 5도 돌림

    #while 반복문을 빠져 나오면 땅에 닿은 상태임
    d = t.distance(target, 0) #거북이와 목표지점과의 거리 저장
    t.sety(r.randint(10, 100)) #성공 또는 실패를 표시할 위치 지정
    if d < 25:
        t.color('blue')
        t.write("Good!", False, "center", ("", 15))  #명중 처리
        #글자쓰기 함수("문자열", 위치 이동않음, 가운데정렬, 글꼴 크기)
    else: #그렇지 않으면 실패한 것으로 처리
        t.color('red')
        t.write("Bad!", False, "center", ("", 15))  # 실패 처리
        t.color('black')
        t.goto(-200, 10)  # 거북이를 처음 위치로 되돌림
        t.setheading(ang) # 각도를 처음 저장한 각도로 되돌림

# 땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점 그리기
target = r.randint(50, 150) # 목표지점은 50~150 사이의 임의의 수
t.color('green')
t.pensize(2)
t.up()   #선 올리기
t.goto(target - 25, 2)  #x좌표, y좌표 : 2
t.down() #선 내리기
t.goto(target + 25, 2)  #x좌표, y좌표 : 2

# 거북이의 처음 위치 설정
t.color('black') #거북이를 검은색으로 변경
t.up()
t.goto(-200, 10)
t.setheading(20) #거북이 머리각도를 20도

# 동작하는 설정
t.onkeypress(turn_up, "Up")  # turn_up 함수 실행
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")  # 발사함수 실행
t.listen()


t.mainloop()
