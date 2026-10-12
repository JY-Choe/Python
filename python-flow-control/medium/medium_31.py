# for + 누적 변수를 사용하세요.
n = int(input())

# 총 합값 초기화
total = 0

# 입력 받은 수까지의 총 합 구하기
# range(1, n+1): 0을 제외하고 1부터 n까지 순회하여 문제 의도를 명확히 표현
for i in range(1,n+1): 
    total += i

# 출력
print(f"1부터 {n}까지의 합: {total}")