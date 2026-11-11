# 나이로 기본 요금을 정하고, 오후면 50% 추가
age = int(input())
time_slot = input()

# 7세 이하 무료
if age <= 7:
    price = 0

# 13세 이하 3000원
elif age <= 13:
    price = 3000

# 18세 이하 5000원
elif age <= 18:
    price = 5000
    
# 19세 이상 8000원
else:
    price = 8000

# 오전 시간 할증 없음
# 오후 시간 요금의 50%(무료대상은 그대로 무료)
if time_slot == "오후":
    if age > 7:
        price += price // 2

# 출력
print(f"나이: {age}세 | 시간대: {time_slot}")
print(f"입장료: {price}원")