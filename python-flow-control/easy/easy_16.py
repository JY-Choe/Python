# 월을 계절로 변환하세요.
month = int(input())

# 계절 값 초기화
season = "겨울"

# 입력 받은 값이 3,4,5월이면 봄
if 3 <= month <= 5:
    season = "봄"

# 6,7,8월이면 여름
elif 6 <= month <= 8:
    season = "여름"

# 9,10,11월이면 가을
elif 9 <= month <= 11:
    season = "가을"

# 출력 값
print(f"{month}월은 {season}입니다.")