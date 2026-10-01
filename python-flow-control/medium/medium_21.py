# if/elif/else + or 연산자를 사용하세요.
month = int(input())

# 1월부터 12월 사이가 아니면
if month > 12:
    weather = "잘못된 입력입니다."

# 3~5월이면 "봄입니다. / 따뜻한 봄이에요! 꽃구경 가세요 🌸"
elif month == 3 or month == 4 or month == 5:
    weather = "봄입니다.\n따뜻한 봄이에요! 꽃구경 가세요 🌸"

# 6~8월이면 "여름입니다. / 더운 여름이에요! 시원하게 보내세요 🌊"
elif month in (6,7,8):
    weather = "여름입니다.\n더운 여름이에요! 시원하게 보내세요 🌊"

# 9~11월이면 "가을입니다. / 선선한 가을이에요! 단풍 구경 가세요 🍂"
elif month == 9 or month == 10 or month == 11:
    weather = "가을입니다.\n선선한 가을이에요! 단풍 구경 가세요 🍂"
    
# 그 외는 "겨울입니다. / 추운 겨울이에요! 따뜻하게 입으세요 ⛄"
else:
    weather = "겨울입니다.\n추운 겨울이에요! 따뜻하게 입으세요 ⛄"

# 결과
print(weather)