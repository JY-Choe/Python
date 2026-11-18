# 콜라츠 추측 과정과 횟수를 출력하세요.
n = int(input())

# 변수 초기화
count = 0

# 입력 받은 수 출력
print(n)

# 무한 반복
while True:
    # 1이 될 때까지 반복
    if n == 1:
        break
    # 짝수 이면 2로 나눈다
    elif n % 2 == 0:
        n //= 2
        
    # 홀수 이면 3을 곱하고 1을 더한다
    else:
        n = n * 3 + 1
    
    # 출력
    print(n)
    count += 1

# 출력
print("횟수:",count)