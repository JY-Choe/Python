# 반복문으로 각 음료 가격을 입력받아 포인트를 누적하세요
n = int(input())

# 초기화
point = 0
stamp = 0

# 가격 입력 받기
for _ in range(n):
    price = int(input())
    # 적립 포인트: 각 음료 가격의 5%(소수점 버림, 정수로 계산)
    point += int(price * 0.05)

# 스탬프: 3잔마다 1개(총 구매 잔수 // 3)
stamp = n // 3

# 출력
print(f"총 구매: {n}잔")
print(f"총 적립 포인트: {point}점")
print(f"스탬프: {stamp}개")