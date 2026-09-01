# float로 입력받아 구간별로 판정하세요.
distance = float(input())

# 교통수단 값에 지하철 대입
transportation = "지하철"

# 입력 받은 값이 2km 미만이면 도보
if distance < 2:
    transportation = "도보"

# 2km 이상 5km 미만이면 자전거
elif distance < 5:
    transportation = "자전거"

# 5km 이상 20km 미만이면 버스
elif distance < 20:
    transportation = "버스"

# 값 출력
print(f"거리: {distance}km")
print(f"추천 교통수단: {transportation}")