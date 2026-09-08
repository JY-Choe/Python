# 누적 곱 변수의 초깃값은 1로 두세요.
n = int(input())

# 결과값 초기화
result = 1

# 1부터 N까지의 모든 수의 곱
for num in range(1, n+1):
    result *= num

print(str(n) + "! = " + str(result))