# while num > 0으로 반복하며 마지막 자리를 꺼내 reverse에 쌓으세요.
num = int(input())

# 변수 초기화
reverse = 0

# 양의 정수를 입력받아 숫자를 뒤집어서 출력
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

# 출력
print(f"뒤집은 숫자: {reverse}")