# ord/chr와 z/Z 순환 처리
text = input()
result = ""

# text 입력 받기
for char in text:
    # 소문자 a ~ z까지 순환 / 입력 받은 값 + 1
    if ord("a") <= ord(char) + 1 <= ord("z"):
        result += chr(ord(char) + 1)

    # z일 경우 다시 a로 이동
    elif ord("z") == ord(char):
        result += chr(ord(char) - 25)

    # 대문자 A ~ Z까지 순환 / 입력 받은 값 + 1
    elif ord("A") <= ord(char) + 1 <= ord("Z"):
        result += chr(ord(char) + 1)    

    # Z일 경우 다시 A로 이동
    elif ord("Z") == ord(char):
        result += chr(ord(char) - 25)
        
    # 알파벳이 아닌 글자는 그대로 출력
    else:
        result += char

# 출력
print("암호:", result)