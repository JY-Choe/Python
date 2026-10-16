# while + if/elif + break/continue를 사용하세요.
money = int(input())

# 무한 반복
while money >= 500:
    
    # 메뉴 화면 출력
    print(f"잔액: {money}원")
    print("1. 물 (500원)\n2. 주스 (1000원)\n3. 커피 (1500원)")
    
    # 메뉴 선택 받음
    menu_select = int(input())
    
    # 입력 받은 수가 1,2,3 / 이외이면 "잘못된 선택입니다."
    if menu_select == 1:
        price = 500
        menu = "물"
    
    elif menu_select == 2:
        price = 1000
        menu = "주스"
    
    elif menu_select == 3:
        price = 1500
        menu = "커피"
    
    else:
        print("잘못된 선택입니다.")
        continue

    # 잔액 >= 가격 이면 잔액 차감후 "x를 선택했습니다."
    if money >= price:
        # 잔액 차감
        money -= price
        print(f"{menu}를 선택했습니다.")  

    # 그렇지 않으면 "잔액이 부족합니다."
    else:
        print("잔액이 부족합니다.")
        break
    
# 반복 종료 후 "남은 금액: xx원"
print(f"남은 금액: {money}원")