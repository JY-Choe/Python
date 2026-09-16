# N을 입력받아 1~N*N 숫자를 N열씩 탭 구분으로 출력하세요.
n = int(input())

# 숫자 초기화
num = 1

# N * N으로 숫자 출력
for row in range(n):  # 행 반복
    row_values = []     # 리스트 생성
    for col in range(n):  # 열 반복
        row_values.append(str(num))
        num += 1
    print('\t'.join(row_values))