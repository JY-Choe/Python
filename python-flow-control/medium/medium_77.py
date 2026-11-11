# 누진세율: 구간별로 나누어 계산하세요
salary = int(input())

# 초기화
bracket_1 = 1200
bracket_2 = 4600

# 각 구간 세율 구하기
if salary <= bracket_1:
    total_tax = salary * 0.06

elif salary <= bracket_2:
    total_tax = (bracket_1 * 0.06) + ((salary - bracket_1) * 0.15)

else:
    total_tax = (bracket_1 * 0.06) + ((bracket_2 - bracket_1) * 0.15) + ((salary - bracket_2) * 0.24)

# 출력
print(f"연봉: {salary}만원")
print(f"세금: {round(total_tax)}만원")