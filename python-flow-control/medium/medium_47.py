# 15의 배수를 먼저 검사해야 함
# 수도코드: 1부터 50까지 3의 배수(Fizz), 5의 배수(Buzz)를 찾음 / 15의 배수 이면 FizzBuzz / 나머지 숫자는 그대로 출력

# 50까지 반복
n = 50

# n까지 반복
for num in range(1, n + 1):
    
    # 15의 배수이면 "FizzBuzz" 출력
    if num % 15 == 0:
        result = "FizzBuzz"
    
    # 3의 배수이면 "Fizz" 출력
    elif num % 3 == 0:
        result = "Fizz"
    
    # 5의 배수이면 "Buzz" 출력
    elif num % 5 == 0:
        result = "Buzz"

    # 그 이외는 숫자 출력
    else:
        result = num

    # 출력
    print(result)