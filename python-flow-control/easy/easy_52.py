# 가로와 세로를 입력받아 별(*) 사각형을 출력하세요.
width = int(input())
height = int(input())

# 열 반복
for _ in range(height):
    
    # 행 반복
    print("*" * width)