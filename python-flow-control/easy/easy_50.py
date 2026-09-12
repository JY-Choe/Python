# 시작단과 끝단을 입력받아 해당 범위의 구구단을 출력하세요.
start = int(input())
end = int(input())

# 시작단에서 끝단까지 반복
for dan in range(start, end + 1):
    print(f"--- {dan}단 ---")
    
    # 구구단 출력
    for num in range(1,10):
        print(f"{dan} x {num} = {dan * num}")