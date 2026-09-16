# for문으로 순회하며 '('와 ')'의 개수를 각각 세세요.
s = input()

# 변수 초기화
open_count = 0
close_count = 0

# "(", ")"의 개수가 같으면 "올바름", 그렇지 않으면 "올바르지 않음"
for char in s:
    if char == "(":
        open_count += 1
    elif char == ")":
        close_count += 1

# 출력
if open_count == close_count:
    print("올바름")
else:
    print("올바르지 않음")