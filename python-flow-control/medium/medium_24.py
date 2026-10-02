# 구간별로 나눠 계산하세요.
usage = int(input())

# usage가 100이하이면 / 전기요금 (usage * 60) / 부가세(전기요금 * 0.1)
if usage <= 100:
    charge = usage * 60
    
# usage가 100 초과 , 200이하이면 / 전기요금(100 * 60 + (usage - 100) * 120)
elif usage <= 200:
    charge = (100 * 60 + (usage - 100) * 120)

# usage가 200 초과이면 / 전기요금(100 * 60 + 100 * 120 + (usage - 200) * 190)
else:
    charge = (100 * 60 + 100 * 120 + (usage - 200) * 190)

# 부가세 공식
surtax = int(charge * 0.1)

# 총 납부 금액
total = charge + surtax

# 전기요금 출력
print(f"전기 요금: {charge}원")

# 부가세 출력
print(f"부가세 (10%): {surtax}원")

# 총 납부 금액 출력
print(f"총 납부 금액: {total}원")