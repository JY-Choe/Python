# i==0 또는 i==n-1 또는 j==0 또는 j==n-1 이면 테두리입니다.
n = int(input())

# 밖에 있는 for문은 행이다
for i in range(1, n + 1):
    if i == 1 or i == n:    # 1행과 마지막행
        print("*" * n)
        
    else:
        print("*"+" " * (n - 2)+"*")