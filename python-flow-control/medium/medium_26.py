# 나이별 요금 결정 후 단체 할인을 판단하세요.
age = int(input())
group_count = int(input())

# 나이가 3세 이하 이면 0원
if age <= 3:
    price = 0

# 나이가 12세 이하이면 15000원
elif age <= 12:
    price = 15000

# 나이가 18세 이하이면 20000원
elif age <= 18:
    price = 20000

# 나이가 64세 이하이면 30000원
elif age <= 64:
    price = 30000

# 그외 10000원
else:
    price = 10000

# 기본 입장료 출력
print(f"기본 입장료: {price}원")

# 인원수가 10명 이상이면 20% 할인 / 단체 할인 적용 (20%)!
if group_count >= 10:
    # 할인된 가격
    discount_price = int(price * 0.8) 
    print("단체 할인 적용 (20%)!")
    print(f"1인 할인가: {discount_price}원")

    # 총 입장료
    total = discount_price * group_count
    print(f"총 입장료: {total}원") # 할인된 총 입장료

# 인원수가 10명 미만인 경우
else:

    # 총 입장료 출력
    total = price * group_count
    print(f"총 입장료: {total}원")