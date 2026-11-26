# 등급별 카운터 5개를 두고 N번 반복하며 입력 점수에 맞는 카운터를 증가시키세요.
n = int(input())

# 변수 초기화
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0

# n번 만큼 반복
for _ in range(n):
    # 점수 입력 받기
    score = int(input())

    # A: 90 이상 100 이하
    if 90 <= score <= 100:
        count_a += 1
    
    # B: 80 이상 89 이하
    elif 80 <= score:
        count_b += 1

    # C: 70 이상 79 이하
    elif 70 <= score:
        count_c += 1

    # D: 60 이상 69 이하
    elif 60 <= score:
        count_d += 1

    # F: 0 이상 59 이하
    else:
        count_f += 1

# 출력
print(f"A (90~100): {count_a}명")
print(f"B (80~89): {count_b}명")
print(f"C (70~79): {count_c}명")
print(f"D (60~69): {count_d}명")
print(f"F ( 0~59): {count_f}명")