# while True 안에서 음수면 break, 아니면 total에 누적.
total = 0

# 음수가 아니라면 입력된 값을 누적시키기
while True:
    # 숫자 입력 받기
    num = int(input())

    if num < 0:
        break # 음수면 즉시 멈춤
    
    # 누적 시킨 값
    total += num

# 출력
print("합계:", total)