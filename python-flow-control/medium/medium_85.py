# for문으로 순회하며 이전 문자와 현재 문자를 비교하세요.
s = input()
result = ""

# 첫 문자로 초기값 설정
prev_char = s[0]
count = 1

# 두번째 문자 부터 순회
for char in s[1:]:
    if char == prev_char:
        count += 1

    else:
        result += f"{prev_char}{count}"
        prev_char = char
        count = 1

# 출력
result += f"{prev_char}{count}"
print(result)