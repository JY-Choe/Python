# 나이 구간별로 구분과 요금을 정하세요.
age = int(input())

# 7세 이하: 무료, 0원
if age <= 7:
    sortation = "무료"
    fare = 0

# 8~13세: 어린이, 5000원
elif age < 14:
    sortation = "어린이"
    fare = 5000

# 14~19세: 청소년, 8000원
elif age < 20:
    sortation = "청소년"
    fare = 8000

# 20~64세: 성인, 12000원
elif age < 65:
    sortation = "성인"
    fare = 12000

# 65세 이상: 경로, 5000원
else:
    sortation = "경로"
    fare = 5000

# 출력
print(f"나이: {age}세")
print(f"구분: {sortation}")
print(f"요금: {fare}원")