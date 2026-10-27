# for + if char != remove: result += char
text = input()
remove = input()
result = ""

# 각각의 문자열로 출력
for char in text:
    if char != remove:  # 삭제할 문제열 제거
        result += char

# 출력
print("결과:", result)