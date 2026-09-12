# while saved < goal: 현재 상태 출력 → 동전 입력 → saved 누적
goal = int(input())
saved = 0

# 첫 줄에 목표 금액 goal을 입력받고, 그 이후 동전 금액을 한 줄씩 입력받아 누적합니다.
while saved < goal:
    print(f"현재: {saved}원 / 목표: {goal}원")
    saved += int(input())
       
# 출력 값
print(f"현재: {saved}원 / 목표: {goal}원")
print(f"목표 달성! 총 {saved}원을 모았습니다.")