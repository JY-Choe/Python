# 30분 초과분을 10분 단위로 올림 청구
print("=== 주차 요금 계산기 ===")
enter_time = int(input())
exit_time = int(input())
parked = exit_time - enter_time

# 기본 요금 설정
fee = 2000

# 추가 요금 설정
add_charge = 0

# 출력
print(f"주차 시간: {parked}분")
print(f"기본 요금: {fee}원")

# 30분 초과 시 추가 시간 표시
if parked > 30:
    # 추가 시간 구하기
    add_time = parked - 30
    print(f"추가 시간: {add_time}분")
    
    # 추가 요금 구하기 / 10분 미만의 나머지도 500원 청구
    if add_time % 10 != 0:
        add_charge = (add_time // 10) * 500 + 500
    
    else:
        add_charge = (add_time // 10) * 500

# 총 요금
total = fee + add_charge

# 출력
print(f"추가 요금: {add_charge}원")
print(f"총 요금: {total}원")