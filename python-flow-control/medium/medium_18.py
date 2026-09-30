# print(값, end="\t")로 탭 구분 출력을 만드세요.
n = int(input())

# "X" 부터 시작
print("X", end="\t")
# 입력 받은 수까지의 곱셈표(행) — 변수명을 col_num으로 변경해 row/col과 일관성 유지
for col_num in range(1, n + 1):
    print(col_num, end="\t")
print()

# "-" 30개 출력
print("-" * 30)

# 입력 받은 수까지의 곱셈표(열)
for row in range(1, n + 1):
    print(row, end="\t")
    # 입력 받은 수까지의 곱
    for col in range(1, n + 1):
        print(col * row, end="\t")
    print()