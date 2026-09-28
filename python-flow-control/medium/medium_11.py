# 바깥 for문은 단, 안쪽 for문은 곱하는 수(1~9)입니다.
a, b = map(int, input().split())

# a단 부터 b단까지 몇 단인지 반복
for n in range(a, b + 1):
    print(f"--- {n}단 ---")
    
    # 입력 받은 구단 출력
    for i in range(1, 10):   # 1~9까지 곱하는 수
        print(f"{n} x {i} = {n * i}")
    
    # 단이 끝나면 빈 줄 출력
    print()