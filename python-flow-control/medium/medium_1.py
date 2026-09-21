# while True 안에서 정답일 때 break 하세요.
answer = 42

# 입력 받은 수가 정답일때 까지 반복 / 정답이 맞으면 종료
while True:
    guess = int(input())

    if guess > answer:
        print("더 작은 수를 입력하세요")

    elif guess < answer:
        print("더 큰 수를 입력하세요")
        
    else:
        print("정답입니다!")
        break