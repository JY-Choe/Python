# range(n, 0, -1)은 n부터 1까지 감소합니다.
n = int(input())

# 입력 받은 수만큼 별을 역삼각형으로 만들어 출력
for num in range(n, 0, -1):
    print("*" * num)