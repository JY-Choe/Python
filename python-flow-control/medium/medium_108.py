# 등급별 카운터 4개를 0으로 초기화하고, 입력 0을 종료 조건으로 반복 처리하세요.
count_a = 0
count_b = 0
count_c = 0
count_f = 0

# 무한 반복
while True:
    # 점수 입력 받기
    score = int(input())

    # score가 0이면 종료
    if score == 0:
        break

    # score가 0보다 작으면 "잘못된 점수"
    elif score < 0:
        print("잘못된 점수")

    # score가 100보다 크면 "점수 초과"
    elif score > 100:
        print("점수 초과")

    # score가 90 ~ 100이면 count_a + 1 
    elif 90 <= score:
        count_a += 1
    
    # score가 80 ~ 89이면 count_b + 1
    elif 80 <= score:
        count_b += 1

    # score가 70 ~ 79이면 count_c + 1
    elif 70 <= score:
        count_c += 1

    # 그 외의 score는 count_f + 1
    else:
        count_f += 1

# 출력
print(f"A: {count_a} B: {count_b} C: {count_c} F: {count_f}")