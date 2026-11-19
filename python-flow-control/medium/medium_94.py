# 홀수 N을 입력받아 마름모를 출력하세요.
n = int(input())

# 중간 값 찾기
mid = n // 2 + 1

# 공백, 별의 index값 구하기
i = mid - 1
j = 1

# n값 만큼 반복
for row in range(1, n + 1):
    # 출력
    print(" " * i + "*" * j)
    
    # 공백, 별의 index값 변경
    if row < mid:  
        i -= 1
        j += 2

    else: 
        i += 1    
        j -= 2