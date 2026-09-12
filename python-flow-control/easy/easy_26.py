# 회원일 때만 VIP 여부를 input()으로 추가로 받으세요.
is_member = input()

# 회원 Y:
if is_member == "Y":

    # 회원일 경우 VIP 여부 파악
    is_VIP = input()

    # VIP Y: 20% 할인 적용
    if is_VIP == "Y":
        print("20% 할인 적용")

    # VIP N: 10% 할인 적용
    else:
        print("10% 할인 적용")

# 회원 N: 할인 없음
else:
    print("할인 없음")