# for + 누적 변수를 사용하세요.
n = int(input())

# 총 합값 초기화
total = 0

# 입력받은 횟수만큼 반복
for _ in range(n):
    # 점수 입력받기
    score = int(input())    # 숫자를 입력받기
    total += score      # 점수 합하기

# 평균 값 구하기
average = total / n

# 출력
print(f"평균 점수: {average}")