# 발견 여부를 추적하는 플래그 변수를 사용합니다. 조건을 만족하는 첫 원소에서 break.
nums = [4, 7, 15, 3, 22, 9]
k = int(input())

# 변수 초기화
found_index = 0
is_found = False

# 입력 받은 수 보다 큰 리스트의 수 찾기
for index, num in enumerate(nums):
    if num >= k:
        found_index = index
        is_found = True
        break

# 플래그 변수를 사용하여 출력
if is_found:
    print("위치:", found_index)
    print("값:", nums[found_index])

else:
    print("찾지 못했습니다")