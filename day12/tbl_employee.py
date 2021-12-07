import sqlite3

def getconn():
    con = sqlite3.connect("c:/pydb/mydb.db") #mydb.db가 없으면 새로 생성되고, 있으면 연결됨
    return con

def select_emp():  # 전체 목록
    conn = getconn()  #db 연결 객체 생성
    cur = conn.cursor()  #db 작업(삽입,추가,변경,삭제) 객체
    sql = "SELECT * FROM employee ORDER BY emp_id"  # db 검색 ,오름차순(asc 생략됨)
    cur.execute(sql)   # 검색 실행
    rs = cur.fetchall()     # 모든 자료 가져오기(result set)
    for i in rs:
        print(i)
    conn.close()       # db 연결 종료 - 필수

def insert_emp():  #자료 추가
    conn = getconn()  # db 연결 객체 생성
    cur = conn.cursor()  # db 작업 객체
    # 입력방법 1 칼럼값을 직접 입력
    # sql = "INSERT INTO employee VALUES ('e1001', '추신수', 40, 40000)" # data 추가
    # 방법2 - ?기호 사용 - 동적 입력
    sql = "INSERT INTO employee VALUES (?, ?, ?, ?)"
    cur.execute(sql, ('e1004', '박인비', 33, 30000))
    conn.commit()   # 커밋 실행 - 필수(데이터에 변경이 생겼을때 반드시 명시)
    conn.close()

def select_one():  #특정 자료 검색
    conn = getconn()
    cur = conn.cursor()
    #sql = "SELECT emp_id, name FROM employee WHERE salary=50000"
    sql = "SELECT name, salary FROM employee WHERE emp_id=?"
    cur.execute(sql, ('e1002', ))   #튜플 구조는 1개를 명시할 때 콤머 찍어야 함
    rs = cur.fetchone()  #1명의 자료 반환
    print(rs)
    conn.close()

def update_emp():  # 자료 수정
    conn = getconn()
    cur = conn.cursor()
    sql = "UPDATE employee SET age = ? WHERE emp_id = ?"
    cur.execute(sql, (33, 'e1004'))
    conn.commit()  #커밋 수행
    conn.close()

def delete_emp(): # 자료 삭제
    conn = getconn()
    cur = conn.cursor()
    sql = "DELETE FROM employee WHERE name = ?"
    cur.execute(sql, ('안산', ))
    conn.commit() #커밋 수행
    conn.close()

if __name__=="__main__":
    #insert_emp()
    #delete_emp()
    update_emp()
    select_emp()  #select_emp() 호출
    #select_one()