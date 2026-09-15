# for문으로 순회하며 모음 여부를 확인하세요.
s = input()
result = ""

# 순회하여 모음 찾기 / 모음이 아닌 다른 문자들을 출력
for char in s:
    if char.lower() in "aeiou":
        continue
    else:
        result += char

# 출력
print(result)