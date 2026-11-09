# for문과 인덱스를 사용하여 금지어를 찾아 대체하세요.
sentence = input()
banned = input()

# 변수 초기화
skip = 0
result = ""

# 금지어 인덱스 값
rest_word = len(banned)

# 인덱스 값을 활용하여 반복
for i in range(len(sentence)):
    # 건너뛰는 값
    if skip > 0:
        skip -= 1
    
    # 그 외
    else:
        # 인덱스 값을 사용하여 금지어("***")로 변경
        if sentence[i : i + rest_word] == banned:
            result += "***"
            skip = rest_word - 1

        # 그 외 값 저장
        else:
            result += sentence[i]

# 출력
print(result)