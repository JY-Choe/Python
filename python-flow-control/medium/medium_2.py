# chance = 3 로 시작, while chance > 0: 입력 → 비교 → 맞으면 break, 틀리면 chance -= 1
password = "python"

# chance 변수에 횟수 대입
chance = 3

# 변수 chance에 입력된 횟수 만큼 반복
while chance > 0:
    user_password = input()

    # 입력받은 비밀번호가 맞으면 "로그인 성공!"
    if user_password == password:
        print("로그인 성공!")
        break

    # 틀리면 횟수 차감 
    else:
        chance -= 1

        # "틀렸습니다. 남은 기회: 00번" 출력
        if chance > 0:
            print("틀렸습니다. 남은 기회:", str(chance) + "번")
            
# 3회 이상 틀리면 "계정이 잠겼습니다" 출력
else:
    print("계정이 잠겼습니다")