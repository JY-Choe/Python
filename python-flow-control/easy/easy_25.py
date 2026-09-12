# 중첩 if문으로 아이디를 먼저, 그 안에서 비밀번호를 확인하세요.
user_id = input()
password = input()

# 아이디 맞음:
if user_id == "admin":
    
    # 비밀번호 맞음: 로그인 성공!
    if password == "1234":
        print("로그인 성공!")

    # 비밀번호 틀림: 비밀번호가 틀렸습니다.
    else:
        print("비밀번호가 틀렸습니다.")

# 아이디 틀림: ID가 존재하지 않습니다.
else:
    print("ID가 존재하지 않습니다.")