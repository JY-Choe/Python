# lower()로 소문자 변환 후 비교
text = input()
vowel_count = 0

# 모음 정의
vowel = "a","e","i","o","u"

# 입력 문자 소문자로 변경
text = text.lower()

# 모음 찾기
for char in text:
    if char in vowel:
        vowel_count += 1

# 출력
print("모음 개수:", vowel_count)