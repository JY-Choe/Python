# 거래 종류를 판별하여 잔액을 관리하세요.
balance = int(input())

# 세번 반복
for i in range(3):
    # 입력 받기
    user_input = input().split()
    menu = user_input[0]
    
    # 입금 / 잔액에 금액을 더한 후 금액 출력
    if menu == "입금":
        money = int(user_input[1])
        balance += money
        print(f"입금 완료: 잔액 {balance}원")
    
    # 출금 / 잔액이 충분하면 빼고 잔액 출력 / 잔액 부족 시 "출금 실패: 잔액 부족" 출력
    elif menu == "출금":
        money = int(user_input[1])
        if balance >= money:
            balance -= money
            print(f"출금 완료: 잔액 {balance}원")
        else:
            print("출금 실패: 잔액 부족")
    
    # 조회 / 현재 잔액 출력
    elif menu == "조회":
        print(f"현재 잔액: {balance}원")

# 마지막 최종 잔액 출력
print(f"최종 잔액: {balance}원")