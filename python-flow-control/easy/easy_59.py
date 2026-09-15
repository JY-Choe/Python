# for문으로 문자열을 순회하며 플래그를 사용하세요.
s = input()

# 플래그 변수 선언
has_at = False
has_dot = False

# 문자열을 입력받아 "@", "." 찾기
for char in s:
    if char == "@":
        has_at = True
    if char == ".":
        has_dot = True
    # 모두 찾았다면 반복할 이유 없음
    if has_at and has_dot:
        break

# 출력
if has_at and has_dot:
    print("유효")
else:
    print("무효")