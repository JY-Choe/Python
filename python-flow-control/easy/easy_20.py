# 1~7 외의 입력은 else로 처리하세요.
day = int(input())

# 1이면 월요일
if day == 1:
    print(f"{day} → 월요일")

# 2이면 화요일
elif day == 2:
    print(f"{day} → 화요일")

# 3이면 수요일
elif day == 3:
    print(f"{day} → 수요일")

# 4이면 목요일
elif day == 4:
    print(f"{day} → 목요일")

# 5이면 금요일
elif day == 5:
    print(f"{day} → 금요일")

# 6이면 토요일
elif day == 6:
    print(f"{day} → 토요일")
    
# 7이면 일요일
elif day == 7:
    print(f"{day} → 일요일")

# 그 외 범위를 벗어나면 "잘못된 입력입니다." 출력
else:
    print("잘못된 입력입니다.")