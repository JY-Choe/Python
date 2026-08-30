# <= 연산자와 if/else를 사용하세요.
battery = int(input())

# 입력 받은 배터리 잔량이 20이하이면 충전 필요
if battery <= 20:
    print("충전 필요")

# 아니면 배터리 충분을 출력
else:
    print("배터리 충분")