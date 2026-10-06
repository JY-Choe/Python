# 연산자를 if/elif로 판별하고 나누기에서 0 체크를 추가하세요.
num1 = float(input())
op = input()
num2 = float(input())

# "/"이면 num2 == 0일 경우 "0으로 나눌 수 없습니다." 출력
if op == "/" and num2 == 0:
    print("0으로 나눌 수 없습니다.")

# "+" 이면 num1 + num2
elif op == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)

# "-" 이면 num1 - num2
elif op == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

# "*" 이면 num1 * num2
elif op == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)

# "/" 이면 num1 / num2
elif op == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)
    
# 이외 연산자이면 "지원하지 않는 연산자입니다." 출력
else:
    print("지원하지 않는 연산자입니다.")