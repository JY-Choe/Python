# 정수를 이진수로 변환하여 1의 개수를 출력하세요. (bin() 사용 금지)
n = int(input())

# 변수 초기화
division = 0

# 무한 반복
while n > 0:
    division += n % 2
    n //= 2

# 출력
print(division + n)