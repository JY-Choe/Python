# 3자리 정수를 입력받아 각 자리를 분해하고 합, 곱을 출력하세요.
num = int(input())

# 백의 자리 구하기
score_100 = num // 100
score = num % 100

# 십의 자리 구하기
score_10 = score // 10

# 일의 자리 구하기
score = score % 10

# 출력
print(f"백의자리: {score_100}")
print(f"십의자리: {score_10}")
print(f"일의자리: {score}")
print(f"합: {(score_100 + score_10 + score)}")
print(f"곱: {(score_100 * score_10  * score)}")