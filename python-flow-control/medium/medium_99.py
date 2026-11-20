# 컴퓨터 패턴과 비교하여 승패를 판정하세요.
n = int(input())

# 변수 초기화
win_count = 0
lose_count = 0
draw_count = 0
count = 1

# n만큼 반복
for i in range(1, n + 1):

    # 입력 받기
    player = input()

    # count가 1이라면 
    if count == 1:
        
        # 값 추가
        count += 1

        # 입력 값이 가위일 경우
        if player == "가위":
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(바위) -> 패")
            lose_count += 1

        # 입력 값이 바위일 경우
        elif player == "바위":
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(바위) -> 무")
            draw_count += 1

        # 입력 값이 보일 경우
        else:
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(바위) -> 승")
            win_count += 1

    # count가 2이라면
    elif count == 2:

        # 값 추가
        count += 1

        # 입력 값이 가위일 경우
        if player == "가위":
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(보) -> 승")
            win_count += 1

        # 입력 값이 바위일 경우
        elif player == "바위":
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(보) -> 패")
            lose_count += 1

        # 입력 값이 보일 경우
        else:
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(보) -> 무")
            draw_count += 1

    # count가 3이라면
    elif count == 3:

        # 값 추가
        count = 1

        # 입력 값이 가위일 경우
        if player == "가위":
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(가위) -> 무")
            draw_count += 1

        # 입력 값이 바위일 경우
        elif player == "바위":
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(가위) -> 승")
            win_count += 1

        # 입력 값이 보일 경우
        else:
            print(f"{i}판: 플레이어({player}) vs 컴퓨터(가위) -> 패")
            lose_count += 1

# 출력
print(f"전적: {win_count}승 {lose_count}패 {draw_count}무")