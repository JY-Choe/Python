# 바깥 if는 회원/비회원, 안쪽 if는 시간 분기로 작성하세요.
is_member = input() == "True"
hours = int(input())

# 변수 초기화
Member_fee = 1000
None_Member_fee = 2000

# 회원이면
if is_member:
    # 1시간 이하: 무료
    if hours <= 1:
        print("무료")

    # 1시간 초과: 초과 1시간당 1000원 → 요금: XXX원
    else:
        extra_fee = Member_fee * (hours - 1)
        print(f"요금: {extra_fee}원")

# 비회원이면
else:
    # 1시간 이하: 요금: 2000원
    if hours <= 1:
        print(f"요금: {None_Member_fee}원")

    # 1시간 초과: 기본 2000원 + 초과 1시간당 2000원 → 요금: XXX원
    else:
        extra_fee = None_Member_fee + None_Member_fee * (hours - 1)
        print(f"요금: {extra_fee}원")