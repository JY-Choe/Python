# 무한 루프 안에서 0 입력 시 BYE 출력 후 break, 그 외는 범위별 분기 후 카운트.
# 변수 초기화
count = 0

# 무한 반복
while True:
    # 좌석 번호 입력 받기
    seat = int(input())

    # 좌석이 0이면 "BYE" 출력후 종료
    if seat == 0:
        print("BYE")
        break

    # 좌석이 1 ~ 10번이면 비즈니스석 출력 후 count 1 추가
    elif 1 <= seat <= 10:
        print("비즈니스석 예약")
        count += 1 

    # 좌석이 11 ~ 20번이면 일반석 출력 후 count 1 추가
    elif 11 <= seat <= 20:
        print("일반석 예약")
        count += 1 

    # 좌석이 21 ~ 30번이면 이코노미석 출력 후 count 1 추가
    elif 21 <= seat <=30:
        print("이코노미석 예약")
        count += 1 

    # 그 외 잘못된 좌석 출력
    else:
        print("잘못된 좌석")

# 출력
print(f"총 예약: {count}건")