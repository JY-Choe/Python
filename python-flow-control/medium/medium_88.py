# for문으로 순회하며 단어를 모으고 공백을 만나면 뒤집으세요.
s = input()
result = ""
word = ""

# 입력받은 s를 순회
for char in s:
    # 공백 발생 시
    if char in " ":
        # word의 내용 뒤집기
        word = word[::-1]
      
        # result에 값 추가
        result += word + char
      
        # word를 다시 공백으로
        word = ""

    # 공백이 아닐 시
    else:
        # 값 추가
        word += char

# 반복이 끝난 후 나머지 값 뒤집기
word = word[::-1]

# result에 값 추가
result += word

# 출력
print(result)