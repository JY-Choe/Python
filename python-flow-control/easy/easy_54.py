# 숫자와 N을 입력받아 2~N의 배수인지 각각 출력하세요.
num = int(input())
n = int(input())

# 입력받은 숫짜까지 반복
for i in range(2, n + 1):
    # 배수 찾기
    if num % i == 0:
        print(f"{i}의 배수입니다.")

    else:
        print(f"{i}의 배수가 아닙니다.")