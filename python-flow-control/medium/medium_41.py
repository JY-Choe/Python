# for + if를 사용하세요.
n = int(input())
count = 0

# 수도 코드: n값 만큼 반복 / 점수를 입력 받음 / 합격자 수를 추출 / 출력

for _ in range(n):
    score = int(input())    # 점수 입력 받기
    if score >= 60:     # 합격 조건
        count += 1      # 합격자 추가

# 출력
print("합격자 수:", count)