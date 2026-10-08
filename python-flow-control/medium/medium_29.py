# 통화를 선택한 뒤 환율에 맞게 계산하세요.
currency = int(input())
krw = int(input())

# 수도 코드: 환전할 통화를 선택 / 선택한 통화로 환전
# 플래그 변수 선언
is_valid = True

# 1 => 달러
if currency == 1:
    charge = round((krw / 1350), 2)     # 요금 계산
    unit = "달러"

# 2 => 엔
elif currency == 2:
    charge = round((krw / 9), 2)    # 요금 계산
    unit = "엔"

# 3 => 유로
elif currency == 3:
    charge = round((krw / 1450), 2)
    unit = "유로"

# 그 외는 "잘못된 통화 선택입니다."
else:
    print("잘못된 통화 선택입니다.")
    is_valid = False

# 1,2,3 이면 실행
if is_valid:
    fee = int(krw * 0.015)
    total = krw + fee
    print(f"환전 금액: {charge} {unit}")
    print(f"수수료 (1.5%): {fee}원")
    print(f"실 지불 금액: {total}원")