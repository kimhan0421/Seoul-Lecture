student_list = []
for i in range(2):  # 3명의 학생을 입력받음
    st = dict()  # 딕셔너리로 선언
    st['name'] = input('이름 : ')
    st['kor'] = int(input('국어 : '))
    st['eng'] = int(input('영어 : '))
    st['mat'] = int(input('수학 : '))
    st['tot'] = st['kor'] + st['eng'] + st['mat']  # 총점을 구하는 식
    st['ave'] = st['tot'] / 3  # 평균 구하는 식
    student_list.append(st)  # 앞서 선언한 student_list에 학생들의 성적 정보를 추가하기
print("이름 국어 영어 수학 총점 평균")

for i in range(len(student_list)):
    st = student_list[i]
    print("%3s %4d %4d %4d %4d %6.2f" %
          (st['name'], st['kor'], st['eng'], st['mat'], st['tot'], st['ave']))

data = sorted(student_list, key=lambda st: (st['ave']), reverse=True)

print("이름 국어 영어 수학 총점 평균")
for i in range(len(data)):
    st = data[i]
    print("%3s %4d %4d %4d %4d %6.2f" %
          (st['name'], st['kor'], st['eng'], st['mat'], st['tot'], st['ave']))
# d : 숫자(digit)
# s : 문자열(str)
# f : 실수 (float)
