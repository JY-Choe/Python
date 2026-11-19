# N개 상품 가격을 입력받아 조건부 할인 후 총액을 출력하세요.
n = int(input())

# 변수 초기화
total_price = 0

# 입력 받은 상품 개수 만큼 가격 입력 받기
for _ in range(n):
    price = int(input())
    # 10000원 이상인 상품만 20% 할인 적용
    if price >= 10000:
        total_price += price * 0.8
    # 10000원 미만인 상품은 원래 가격 그대로 합산
    else:
        total_price += price

# 정수로 변환
total_price = int(total_price)

# 출력
print(f"총액: {total_price}원")