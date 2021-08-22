# 2

dan = int(input())
for index in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    result = dan * index
    print(dan, '*', index, '=', result)


# N = int(input())
# for i in range(1, 10):
#     print(N, "*", i, "=", N*i)

# N = int(input())
# T = int(input())

# print(N, "*", T, "=", N*T)


# 3

n = int(input())

for i in range(1, n+1):

    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", end=" ")

    else:
        print(i, end=" ")
