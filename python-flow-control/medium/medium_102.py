# N번 반복하며 점수를 입력받습니다. 범위를 벗어나면 안내 출력 후 continue, 유효한 점수만 누적합에 더하세요.
# 반복문 종료 후 최종 합계를 한 줄 출력합니다.
n = int(input())
total = 0

# n 값만큼 입력 받기
for _ in range(n):
    score = int(input())
    # 0 이상 100 이하 인 점수만 유효
    if 0 <= score <= 100:
        # 유효한 점수는 합계에 누적
        total += score
    # 유효하지 않은 점수가 들어오면 "무효: x" 형식으로 continue
    else:
        print(f"무효: {score}")
        continue
    
# 모든 입력이 끝난 뒤 마지막 줄에 "유효 점수의 합: x" 형식으로 출력
print(f"유효 점수의 합: {total}")