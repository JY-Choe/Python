# 바깥 if는 배차 가능 여부, 안쪽 if는 목적지 유무로 작성하세요.
available = input() == "True"
destination = input()

# 배차 가능이면
if available:
    # 목적지가 있다면
    if destination:
        print("운행 시작")
        
    # 목적지가 없다면
    else:
        print("목적지를 입력하세요")

# 배차가 불가능 하다면
else:
    print("차량 대기 중")