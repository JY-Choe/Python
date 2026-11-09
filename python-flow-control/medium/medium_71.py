# 교시별 과목 배정 후 표 형태로 출력하세요.
n = int(input())

# 1 ~ 6교시의 "-"의 시간표 만들기
class_list = ["-"] * 6

# n번까지 반복
for _ in range(n):
    # subject, start, end값 입력 받기
    subject, start, end = input().split()

    # 정수로 변경
    start = int(start)
    end = int(end)

    # 입력 받은 값 리스트에 삽입
    for i in range(start - 1, end):
        if class_list[i] == "-":
            class_list[i] = subject

# 출력
print("교시 | 과목")
print("-----|------")

for index, subjects in enumerate(class_list, 1):
    print(f"{index}교시 | {subjects}")