# 나이로 기준을 먼저 나누세요.
height = float(input())
weight = float(input())
age = int(input())

# BMI 공식
bmi = weight / ((height / 100) ** 2)

# 성인이면
if age >= 20:
    # BMI가 18.5 미만이면 "판정: 저체중"
    if bmi < 18.5:
        judgment = "판정: 저체중"
        
    # BMI가 23 미만이면 "판정: 정상"
    elif bmi < 23:
        judgment = "판정: 정상"

    # BMI가 25 미만이면 "판정: 과체중"
    elif bmi < 25:
        judgment = "판정: 과체중"

    # 그 외 "판정: 비만"
    else:
        judgment = "판정: 비만"


# 청소년이면
else:
    # BMI가 17 미만이면 "판정: 저체중 (청소년 기준)"
    if bmi < 17:
        judgment = "판정: 저체중 (청소년 기준)"

    # BMI가 23 미만이면 "판정: 정상 (청소년 기준)"
    elif bmi < 23:
        judgment = "판정: 정상 (청소년 기준)"

    # 그 외 "판정: 과체중 주의 (청소년 기준)"
    else:
        judgment = "판정: 과체중 주의 (청소년 기준)"

# BMI 출력
print(f"BMI: {bmi:.2f}")

# 판정 결과 출력
print(judgment)