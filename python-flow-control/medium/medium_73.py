# 7일 초과분에 대해 일당 200원 부과
days = int(input())

# 대여 요금 계산
if days <= 7:
    charge = 0
else:
    charge = (days - 7) * 200

# 출력
print(f"대여 일수: {days}일")
print(f"대여료: {charge}원")