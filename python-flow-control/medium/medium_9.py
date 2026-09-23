# 바깥 for문으로 줄, 안쪽 for문으로 별 개수를 제어하세요.
n = int(input())

# 입력 받은 값 한 줄에 한개씩 출력
for line_num in range(1, n + 1):
    print("*" * line_num)