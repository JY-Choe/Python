# i = 1, while i <= n: total += i; i += 1
n = int(input())

# 변수 초기화
total = 0

# 1부터 입력받은 N값까지의 합을 출력
i = 1

while i <= n:
    total += i
    i += 1

print(f"1부터 {n}까지의 합: {total}")