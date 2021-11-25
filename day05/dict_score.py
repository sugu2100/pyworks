# 학생의 성적 합계 및 평균
# 대응 서식 문자 - 정수 : %d, 실수 : %f, 문자열 : %s
student = [
    {'name':'김하나', 'kor':80, 'math':70, 'eng':90},   #1명의 세 과목의 점수
    {'name':'이두울', 'kor':60, 'math':50, 'eng':40},
    {'name':'박세엣', 'kor':90, 'math':90, 'eng':100}
]

# 개인별 총점과 평균
print(" 이름  총점 평균")
for s in student:
    sum_v = s['kor'] + s['math'] + s['eng']
    avg = sum_v / 3
    print("%s %d %.1f" % (s['name'], sum_v, avg))

# 과목별 총점과 평균
sum_subj = [0, 0, 0]   # 합계 리스트로 초기화
avg_subj = [0.0, 0.0, 0.0] #평균 리스트

for s in student:
    sum_subj[0] += s['kor']
    sum_subj[1] += s['math']
    sum_subj[2] += s['eng']

avg_subj[0] = sum_subj[0] / 3
avg_subj[1] = sum_subj[1] / 3
avg_subj[2] = sum_subj[2] / 3

print("국어 합계 : %d점" % sum_subj[0])
print("수학 합계 : %d점" % sum_subj[1])
print("영어 합계 : %d점" % sum_subj[2])

print("국어 평균 : %.1f점" % avg_subj[0])
print("수학 평균 : %.1f점" % avg_subj[1])
print("영어 평균 : %.1f점" % avg_subj[2])