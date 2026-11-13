# for문과 플래그 변수를 사용하세요. upper() 메서드를 활용하세요.
s = input()
result = ""

# 플래그 변수 초기화
is_found = False

# 첫 글자만 대문자로 출력, 공백 뒤에 오는 글자는 첫 글자
for index in range(len(s)):
    if index == 0 or is_found:
        result += s[index].upper()
        is_found = False

    elif s[index] == " ":
        is_found = True
        result += s[index]
        
    else:
        result += s[index]

# 출력
print(result)