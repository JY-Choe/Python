# for + if/elif/else + 카운팅 변수를 사용하세요.
a_count = 0
b_count = 0
c_count = 0
d_count = 0

# 수도코드: 10번 반복 / 점수 입력받기 / 점수별로 등급 나누기 / 등급별 인원 수 출력
# 10번 반복
n = 10

for _ in range(n):
    # 숫자 입력 받기
    score = int(input())

    # 90점 이상
    if score >= 90:
        a_count += 1

    # 80점 이상
    elif score >= 80:
        b_count += 1

    # 70점 이상
    elif score >= 70:
        c_count += 1

    # 70점 미만
    else:
        d_count += 1

# 출력
print(f"90점 이상: {a_count}명")
print(f"80점 이상: {b_count}명")
print(f"70점 이상: {c_count}명")
print(f"70점 미만: {d_count}명")