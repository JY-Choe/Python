# for문으로 순회하며 '_' 다음 문자를 대문자로 변환하세요.
s = input()
result = ""

# 플래그 변수 초기화
is_found = False

# s의 문자열을 입력받아 언더스코로 연결된 문자열을 카멜케이스로 변경
for char in s:
    if char == "_":
        is_found = True
        continue

    if is_found:
        result += char.upper()
        is_found = False
    
    else:
        result += char

# 출력
print(result)