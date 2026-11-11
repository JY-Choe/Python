# 기본료에 무게 추가, 거리 추가를 더하세요
weight = int(input())
dist = int(input())

# 기본요금
original_fee = 3000

# 2kg이하
if weight <= 2:
    weight_fee = 0

# 2kg 초과 ~ 10kg 이하: 1000원 추가
elif weight <= 10:
    weight_fee = 1000

# 10kg 초과: 3000원 추가
else:
    weight_fee = 3000

# 50km 이하
if dist  <= 50:
    dist_fee = 0

# 50km 초과 ~ 100km 이하: 1500원 추가
elif dist <= 100:
    dist_fee = 1500
    
# 100km 초과: 3000원 추가
else:
    dist_fee = 3000

# 최종 가격
total_fee = original_fee + weight_fee + dist_fee

# 출력
print(f"무게: {weight}kg | 거리: {dist}km")
print(f"택배 요금: {total_fee}원")