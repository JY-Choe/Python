# 인덱스를 알아야 하므로 range로 순회하세요. 글자의 대소문자 변환은 문자열 메서드를 사용합니다.
text = input()

# 변수 초기화
result = ""

# 인덱스로 순회
for i in range(len(text)):
    # 짝수 인덱스의 경우 대문자로 변경
    if i % 2 == 0:
        result += text[i].upper()

    # 그 외는 소문자
    else:
        result += text[i]

# 출력
print(result)