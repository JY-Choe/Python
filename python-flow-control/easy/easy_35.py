# for + range(1, n+1)로 누적합을 구한 뒤, print("1부터", n, "까지의 합:", total)로 출력하세요.
n = int(input())

# 결과 값 초기화
result = 0

# 입력 받은 수까지의 합 구하기
for i in range(1, n + 1):
    result += i
print(f"1부터 {n} 까지의 합: {result}")