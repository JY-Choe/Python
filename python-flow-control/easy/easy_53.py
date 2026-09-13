# N개의 숫자를 입력받아 양수 합, 음수 합, 전체 합을 출력하세요.
n = int(input())

# 변수 초기화
positive_num = 0
negative_num = 0
total = 0

# 숫자 입력 받기 반복
for _ in range(n):
    num = int(input())
    # 양수를 찾음
    if num > 0:
        positive_num += num
    # 찾은 양수의 합
    elif num < 0:
        negative_num += num

# 양수와 음수의 합
total = positive_num + negative_num

# 출력
print(f"양수 합: {positive_num}")
print(f"음수 합: {negative_num}")
print(f"전체 합: {total}")