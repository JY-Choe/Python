# for + if(i % m == 0) + 누적 변수를 사용하세요.
n = int(input())
m = int(input())

# 누적 합 초기화
total = 0

# 수도코드: 입력 받은 수까지 반복 / 입력 받은 수의 배수를 구함 / 배수의 합을 구함 / 출력
for i in range(m, n + 1, m):
    total += i  # 누적 합

# 출력
print(f"1부터 {n}까지 {m}의 배수의 합: {total}")