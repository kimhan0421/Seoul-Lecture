def add(a, b):
    return a+b


def sub(a, b):
    return a-b


# print(add(1, 4))
# print(sub(4, 2))

# print(__name__)  # 해당 모듈의 이름을 가지고 있는 변수

# 이 부분을 추가합니다.
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
