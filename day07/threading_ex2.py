# 일정 시간 후에 타이머 종료
import datetime
import threading

def call():
    print("타이머 종료!!")
    print(datetime.datetime.now()) #call 후의 시간

print(datetime.datetime.now())   #현재 날짜와 시간
timer = threading.Timer(10, call)
timer.start()