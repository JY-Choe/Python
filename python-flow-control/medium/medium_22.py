# 거리 계산 후 야간 여부를 추가 판단하세요.
distance = float(input())
hour = int(input())

# 기본요금
price = 4800

# 기본요금 출력
print(f"기본요금: {price}원")

# 2km 이상 이면
if distance > 2:
    over_distance = int((distance - 2) * 1000)

# 이하이면
else:
    over_distance = 0

# 추가요금 출력
print(f"추가요금: {over_distance}원")

# 야간 할증 시간 / 야간 할증 출력
if hour >= 22 or hour < 6:
    over_hour = int((price + over_distance) * 0.2)
    print(f"야간 할증 (20%): {over_hour}원")
    
# 야간 할증 시간이 아니라면
else:
    over_hour = 0

# 총 택시비 / 출력
total = price + over_distance + over_hour
print(f"총 택시비: {total}원")