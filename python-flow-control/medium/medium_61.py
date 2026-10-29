# N명에 대해 이름, 상태를 반복 입력받아 분류
n = int(input())

# 변수 초기화
present = 0
absent = 0

# 입력 받은 값 만큼 반복
for _ in range(n):
    # 입력 받기
    name = input()
    status = int(input())

    # status값이 1이면 출석
    if status == 1:
        print(f"{name} - 출석")
        present += 1

    # 0이면 결석
    else:
        print(f"{name} - 결석")
        absent += 1

# 출력
print("--- 출석 결과 ---")
print("출석:", present, "명")
print("결석:", absent, "명")