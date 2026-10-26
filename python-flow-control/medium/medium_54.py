# range(len(text)-1, -1, -1)로 역순 순회
text = input()
result = ""

# 문자열 뒤집기
for i in range(len(text)-1, -1, -1):
    result += text[i]
    
# 출력
print("뒤집은 문자열:", result)