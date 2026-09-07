# "N의 약수: "를 end=" "로 출력한 뒤, 1부터 N까지 나머지가 0인 수를 end=" "로 출력하세요.
n = int(input())

# 출력
print(f"{n}의 약수: ", end="")

# 약수 구하기
for divisor in range(1, n + 1):
    if n % divisor == 0:
        print(divisor,end=" ")