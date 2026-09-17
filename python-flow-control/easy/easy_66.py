# 누적합 변수를 두고, K 이하인 원소는 continue로 건너뛰세요.
nums = [3, -2, 5, 0, -7, 4, -1, 6]
k = int(input())

# 변수 초기화
total = 0

# 리스트의 수 중 k 이하인 값은 건너뜀 / 그 외의 값은 합산
for num in nums:
    if num <= k:
        continue
    else:
        total += num

# 출력
print("합계:", total)