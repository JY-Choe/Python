# 3번 반복하며 계산 결과를 누적하세요.
total = 0

# 3번의 연산 수행 계산기
for _ in range(3):
    num1, operator, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)

    # operator가 "+"이면
    if operator == "+":
        plus = (num1 + num2)
        total += plus
        print(plus)

    # operator가 "-"이면
    elif operator == "-":
        minus = (num1 - num2)
        total += minus
        print(minus)

    # operator가 "*"이면
    elif operator == "*":
        multiply = (num1 * num2)
        total += multiply
        print(multiply)

    # operator가 "/"이면
    elif operator == "/":
        division = (num1 // num2)
        total += division
        print(division)

# 출력
print(f"합계: {total}")