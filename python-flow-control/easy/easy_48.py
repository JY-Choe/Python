# max_val = -1로 초기화하고, 입력을 받아가며 현재 값이 더 크면 갱신하세요.

# max_val -1로 초기화
max_val = -1

# max_num 초기화
max_num = False

# 무한 반복
while True:
    # 숫자 입력받기
    num = int(input())
    
    # -1이 입력되면 종료
    if num == -1:
        break

    # 입력한 수중 가장 큰 값을 최대값으로 출력
    if max_num is False or num > max_num:
        max_num = num

# 출력
if max_num is False:  # 유효 입력이 없었던 경우
    print("입력한 숫자가 없습니다.")
    
else:
    print(f"최대값: {max_num}")