# float로 입력받아 구간별 옷차림을 결정하세요.
temp = float(input())

# 변수 초기화
clothes = ""

# 5도 미만: 패딩, 두꺼운 목도리
if temp < 5:
    clothes = "패딩, 두꺼운 목도리"

# 5도 이상 10도 미만: 코트, 니트
elif temp < 10:
    clothes = "코트, 니트"

# 10도 이상 20도 미만: 자켓, 가디건
elif temp < 20:
    clothes = "자켓, 가디건"

# 20도 이상 28도 미만: 반팔, 얇은 셔츠
elif temp < 28:
    clothes = "반팔, 얇은 셔츠"
    
# 28도 이상: 민소매, 반바지
else:
    clothes = "민소매, 반바지"

# 출력
print(f"현재 기온: {temp}°C")
print(f"추천 옷차림: {clothes}")