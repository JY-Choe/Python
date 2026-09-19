# 검증용 while 루프와 자릿수 분해용 while 루프 두 개를 순차로 사용하세요 (중첩 아님).
# 변수 초기화
total = 0

# 검증용 루프
while True:
    number = int(input())
    if number > 0:
        break
    print("양의 정수를 입력하세요")

# 자릿수 분해용 루프
while number > 0:
    total += number % 10
    number //= 10

# 출력
print(total)