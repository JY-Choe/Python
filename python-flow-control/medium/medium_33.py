# for + if + 누적 변수를 사용하세요.
total = 0

# 1 부터 100까지의 숫자 중 홀수의 합 구하기
for i in range(1, 101, 2): # 1부터 홀수 숫자만 가져오기
    total += i

# 출력
print(f"1부터 100까지 홀수의 합: {total}")