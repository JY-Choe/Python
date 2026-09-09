# 누적 곱 변수의 초깃값은 1로 두고, count번 반복하며 입력받은 숫자를 곱하세요.
count = int(input())

# 변수의 초깃값 1
result = 1

# count만큼 반복
for _ in range(count):
    # 입력 받기
    num = int(input())
    
    # 누적 곱
    result *= num

# 출력
print(f"누적 곱: {result}")