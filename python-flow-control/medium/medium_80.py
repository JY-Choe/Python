# 22시 이후 시간을 구분하여 야간수당을 계산하세요
wage = int(input())
hours = int(input())
start = int(input())

# 근무 시간
print(f"시급: {wage}원 | 근무: {hours}시간 ({start}시 시작)")

# 기본급 / 초과 수당 계산
over_time = hours + start - 22
if over_time > 0:
    basic_time = hours - over_time
    over_fee = over_time * 1.5 * wage

else:
    basic_time = hours
    over_fee = 0

# 기본급 출력
basic_fee = int(basic_time * wage + over_fee)
print(f"기본급: {basic_fee}원")

# 주휴수당: 기본급(야간 할증 포함)의 20% 추가 지급
holiday_fee = int(basic_fee * 0.2)
print(f"주휴수당: {holiday_fee}원")

# 최종급여 출력
total_fee = basic_fee + holiday_fee
print(f"총 급여: {total_fee}원")