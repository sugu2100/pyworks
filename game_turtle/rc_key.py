# 키보드로 조종하기
import turtle as t

def turn_right():
    t.setheading(0)   #거북이의 머리 0도
    t.forward(10)

def turn_up():
    t.setheading(90)   #거북이의 머리 90도
    t.forward(10)

def turn_left():
    t.setheading(180)   #거북이의 머리 180도
    t.forward(10)

def turn_down():
    t.setheading(270)   #거북이의 머리 270도
    t.forward(10)

def clear():
    t.clear()

t.shape('turtle')
t.onkeypress(turn_right, "Right")  #오른쪽 화살키
t.onkeypress(turn_up, "Up")        #위쪽 화살키
t.onkeypress(turn_left, "Left")    #왼쪽 화살키
t.onkeypress(turn_down, "Down")    #아래쪽 화살키
t.onkeypress(clear, "Escape")      #선 모두 지우기
t.listen()                         #실행 대기

t.mainloop()
