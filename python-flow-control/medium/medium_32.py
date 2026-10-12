# for + if + 카운팅 변수를 사용하세요.
n = int(input())

# 개수 초기화
count = 0

# 입력 받은 수까지의 짝수의 개수를 찾아 출력
for i in range(1, n + 1):    # 1부터 시작   
    if i % 2 == 0:   # 짝수 구하는 식
        count += 1

# 출력
print(f"1부터 {n}까지 짝수의 개수: {count}")