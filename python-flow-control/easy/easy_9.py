# 컴퓨터는 "바위" 고정. 사용자 입력과 비교하여 결과를 출력하세요.
computer = "바위"
user = input()

# 컴퓨터 값 출력
print(f"컴퓨터: {computer}")

#사용자 값 출력
print(f"나: {user}")

# 사용자가 바위이면 비겼습니다
if user == "바위":
    print("결과: 비겼습니다")

# 사용자가 가위이면 졌습니다
elif user == "가위":
    print("결과: 졌습니다")

# 사용자가 보면 이겼습니다
elif user == "보":
    print("결과: 이겼습니다")

# 그 외 입력은 잘못된 입력입니다 출력
else:
    print("결과: 잘못된 입력입니다")