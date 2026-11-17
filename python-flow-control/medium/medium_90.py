# 정수를 소인수분해하여 결과를 출력하세요.
n = int(input())

# 변수 초기화
divisor = 2

# list 초기화
factorization = []

# 무한 반복
while True:
    # 소인수 분해
    if n % divisor == 0:
        # 값 저장
        factorization.append(str(divisor))
        # 값 변경
        n //= divisor

    # 값 추가
    else:
        divisor += 1

    # 종료
    if n == 1:
        break

# 출력
print(' x '.join(factorization))