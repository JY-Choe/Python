"""
TITLE: BMI 판정
DIFFICULTY: easy
TAGS: if, elif, else, float, calculation

EVAL: stdio

DESCRIPTION:
키(cm)와 몸무게(kg)를 실수로 입력받아 BMI를 계산하고 세 줄로 출력하시오.

```
키: {키}cm, 몸무게: {몸무게}kg
BMI: {BMI를 소수 둘째 자리까지 반올림}
판정: {판정}
```

BMI 계산: 몸무게 / (키/100)^2
판정 기준:
- 18.5 미만: 저체중
- 18.5 이상 23 미만: 정상
- 23 이상 25 미만: 과체중
- 25 이상: 비만

예시:
- 입력: `170\n65` → 출력: `키: 170.0cm, 몸무게: 65.0kg\nBMI: 22.49\n판정: 정상`
- 입력: `160\n45` → 출력: `키: 160.0cm, 몸무게: 45.0kg\nBMI: 17.58\n판정: 저체중`
"""

# cm를 m로 변환한 후 BMI = weight / (height_m ** 2). round(bmi, 2) 사용.
height = float(input())
weight = float(input())

# BMI 계산
BMI = round((weight / (height/100) ** 2),2)

# 18.5 미만: 저체중
if BMI < 18.5:
    judgment = "저체중"

# 18.5 이상 23 미만: 정상
elif BMI < 23:
    judgment = "정상"

# 23 이상 25 미만: 과체중
elif BMI < 25:
    judgment = "과체중"

# 25 이상: 비만
else:
    judgment = "비만"

# 키, 몸무게 / BMI / 판정 출력
print(f"키: {height}cm, 몸무게: {weight}kg")
print(f"BMI: {BMI}")
print(f"판정: {judgment}")