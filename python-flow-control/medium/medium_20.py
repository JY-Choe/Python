# for + if + 누적 변수를 사용하세요.
total = 0
best = 0

# 5명의 횟수 반복
for _ in range(5):
    # 점수 입력 받기
    score = int(input())
    # 합계 누적
    total += score
    # 최고점 갱신
    if score > best:
        best = score

# 평균 값 구하기 (합계와 구분하기 위해 별도 변수 사용)
average = total / 5

# 평균 값 출력
print(f"평균: {average}")

# 최고점 출력
print(f"최고점: {best}")