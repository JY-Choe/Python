# 출석일 수를 카운트한 뒤 백분율을 계산하고, 소수점 첫째 자리까지 포맷팅 출력하세요.
record = input()

# 변수 초기화
count = 0

# 입력 받은 record 하나씩 불러오기
for r in record:
    # 출석한 횟수 구하기
    if "O" in r:
        count += 1

# 출석률 구하기
attendance_rate = count / len(record) * 100

# 출력
print(f"출석률: {attendance_rate:.1f}%")