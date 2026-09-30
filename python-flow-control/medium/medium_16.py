# range(i, 0, -1)로 i부터 1까지 역순 출력하세요.
n = int(input())

# 출력 반복 횟수
for i in range(n, 0, -1):
    for num in range(i, 0, -1):   # 숫자 출력
        print(num, end="")
    print()