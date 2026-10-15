# while문과 %10, //10을 사용하세요.
num = int(input())

# 나머지 값 초기화
division = 0

# 수도코드: 입력 받은 숫자의 나머지를 구함 / 10을 나누어 자리 수 줄이기 / 다 줄이면 출력

while num >= 1:
    division += num % 10    # 나머지 합 구하기
    num //= 10  # 자릿 수 줄이기

# 출력
print(f"각 자릿수의 합: {division}")