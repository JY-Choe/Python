# 누적합 변수와 발견 플래그를 두고, 매 원소를 더한 직후 K 초과 여부를 검사합니다.
nums = [3, 5, 2, 8, 1, 4, 6, 7]
k = int(input())

# 변수 초기화
is_found = False
total = 0
found_index = 0

# 리스트의 합이 입력 받은 수를 초과 하면 멈춤
for index, num in enumerate(nums):
    total += num
    found_index = index
    if total > k:
        is_found = True
        break

# 플래그 변수를 사용하여 출력
if is_found:
    print("위치:", found_index)
    print("누적합:", total)

else:
    print("한계 미달")