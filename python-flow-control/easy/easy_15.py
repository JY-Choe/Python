# if/elif/else로 등급을 판정하세요.
score = int(input())

# 등급 값 초기화
grade = ""

# 입력 받은 점수가 90이상이면 등급 A
if score >= 90:
    grade = "A"

# 80이상이면 B
elif score >= 80:
    grade = "B"

# 70이상이면 C
elif score >= 70:
    grade = "C"

# 60이상이면 D
elif score >= 60:
    grade = "D"

# 60미만이면 F
else:
    grade = "F"
    
# 출력 값
print(f"점수: {score}")
print(f"등급: {grade}")