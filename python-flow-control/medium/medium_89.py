# for문으로 순회하며 ord(), chr()을 사용해 13칸 밀기를 구현하세요.
s = input()
result = ""

# s값 불러오기
for char in s:
    # 소문자 값 변경 후 저장
    if ord("a") <= ord(char) <= ord("z"):
        lower = ord(char) + 13
    
        # lower의 값이 "z"값 보다 클 경우
        if lower > ord("z"):
            lower -= 26
       
        result += chr(lower)
        
    # 대문자 값 변경 후 저장
    elif ord("A") <= ord(char) <= ord("Z"):
        upper = ord(char) + 13

        # upper의 값이 "Z"값 보다 클 경우
        if upper > ord("Z"):
            upper -= 26
          
        result += chr(upper)

    # 그 외 문자 저장
    else:
        result += char

# 출력
print(result)