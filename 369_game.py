# 3

# n = int(input())

# for i in range(1, n+1):

#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         print("X", end=" ")

#     else:
#         print(i, end=" ")


# 실습3 파이썬 369게임 만들기
# 주제 : 반복문, 제어문

# 프로그램 시나리오
# 1. 프로그램 및 사용방법 설명
# 2. 사용자에게 1부터 x까지 출력할 x값 입력받기
# 3. 1부터 x까지 출력, 단 [3, 6, 9] 중 하나의 값이 있다면 별표(*) 출력

print('369 게임 원하는 숫자를 입력하세요.')

# result = [] # 위 코드와 동일
result = list()  # 빈 list 자료형 변수 생성 방법

st_cnt = 0
number = int(input('숫자 입력 : '))
for index in range(1, number + 1):
    if '3' in str(index):
        result.append('*')
        st_cnt += 1
    elif '6' in str(index):
        result.append('*')
        st_cnt += 1
    elif '9' in str(index):
        result.append('*')
        st_cnt += 1
    else:
        result.append(index)

    # if '3' in str(index) or '6' in str(index) or '9' in str(index):
    #     result.append('*')  # list 자료형의 append()는 값을 추가하는 방법
    # else:
    #     result.append(index)
# print(result)  # 변수값 확인 부분

# 출력 부분

cnt = 0
for index in result:
    if index % 10 == 0:
        print(index, end='\n')
    else:
        print(index, end=', ')
    cnt += 1

print('st', st_cnt)
