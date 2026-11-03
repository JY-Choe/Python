# while True 안에서 guess 입력, tries += 1, 비교/break
answer = 42
tries = 0
print("=== 숫자 맞추기 게임 (1~100) ===")

# 무한 반복
while True:
    # 숫자 입력 받음
    guess = int(input())

    # 시도 횟수 파악하기
    tries += 1

    # 입력 값이 정답 값 보다 작은 경우
    if guess < answer:
        print("UP!")

    # 입력 값이 정답 값 보다 큰 경우
    elif guess > answer:
        print("DOWN!")
        
    # 정답이면 종료
    else:
        break
        
# 루프 탈출 후 출력
print(f"정답입니다! 시도 횟수: {tries}번")