# N을 입력받아 1~N에서 3의 배수, 5의 배수, 공배수 개수를 세어 출력하세요.
n = int(input())

# 변수 초기화
count_3 = 0
count_5 = 0
count_15 = 0

# 수도코드: 숫자를 입력받음 / 3, 5의 배수 / 3, 5의 공배수 개수 출력
# 1부터 n까지 반복
for multiple in range(1, n + 1):
    # 3의 배수
    if multiple % 3 == 0:
        count_3 += 1

    # 5의 배수
    if multiple % 5 == 0:
        count_5 += 1

    # 3과 5의 공배수
    if multiple % 15 == 0:
        count_15 += 1

# 출력
print(f"3의 배수: {count_3}개")
print(f"5의 배수: {count_5}개")
print(f"3과 5의 공배수: {count_15}개")