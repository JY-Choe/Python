# while True와 if/elif/break를 사용하세요.
total = 0

# 가격 초기화
price = 0

# 결과 값 문자열로 초기화
result = ""

# 메뉴가 멈출때 까지 반복
while True:
    # 메뉴 출력
    print("--- 메뉴 ---\n1. 아메리카노 (4000원)\n2. 카페라떼 (4500원)\n3. 녹차 (3500원)\n0. 주문 완료")
    
    # 메뉴 선택 받기
    menu = int(input())

    # 1번이면 "아메리카노를 추가했습니다." / 가격 4000
    if menu == 1:
        result = "아메리카노를 추가했습니다."
        price = 4000

    # 2번이면 "카페라떼를 추가했습니다." / 가격 4500
    elif menu == 2:
        result = "카페라떼를 추가했습니다."
        price = 4500

    # 3번이면 "녹차를 추가했습니다." / 가격 3500
    elif menu == 3:
        result = "녹차를 추가했습니다."
        price = 3500

    # 0번이면 종료
    elif menu == 0:
        break

    # 총 합
    total += price

    # 입력 받은 메뉴 출력
    print(result)

# 총 가격 출력    
print(f"총 주문 금액: {total}원")