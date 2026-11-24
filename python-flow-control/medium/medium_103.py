# 누적합 변수와 발견 플래그를 둡니다.
# 한 원소를 살필 때 0이면 즉시 continue, 그 외에는 누적합에 더한 직후 K 도달 여부를 검사하세요.
# 반복문 종료 후 플래그로 "한계 미달" 여부를 판정합니다.
nums = [4, 0, 3, 0, 0, 7, 2, 0, 8, 1]
k = int(input())

# 변수 초기화
total = 0

# 리스트의 수를 하나씩 출력
for i ,num in enumerate(nums):
    
    # 0 인 원소를 만나면 "무시한 위치: x" 한 줄을 출력 / continue
    if num == 0:
        print(f"무시한 위치: {i}")
        continue
    
    # 0이 아닌 원소는 누적 합 total에 더함
    total += num
    
    # 누적 합이 처음 K이상이 되는 순간 (total >= K) 두 줄을 출력하고 break
    if total >= k:
        print(f"종료 위치: {i}")
        print(f"최종 누적합: {total}")
        break

# 끝까지 누적 합이 K미만이면 마지막 줄에 "한계 미달, 누적합: x" 한줄만 출력
else:
    print(f"한계 미달, 누적합: {total}")