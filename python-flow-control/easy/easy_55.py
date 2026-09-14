# 총 초를 입력받아 HH:MM:SS 형식으로 출력하세요.
total_seconds = int(input())

# 시간 구하기
hour = total_seconds // 3600
hour_division = total_seconds % 3600

# 분 구하기
minute = hour_division // 60

# 초 구하기
second = hour_division % 60

# 출력
print(f"{hour:02d}:{minute:02d}:{second:02d}")