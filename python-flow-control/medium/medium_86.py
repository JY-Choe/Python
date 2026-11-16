# while 또는 for + range를 사용하여 인덱스로 접근하세요.
s1 = input()
s2 = input()
result = ""

# 각 입력 값의 길이 구하기
s1_len = len(s1)
s2_len = len(s2)

# 두 길이 중 긴쪽의 값 구하기
max_len = max(s1_len, s2_len)

# index만큼 반복
for i in range(max_len):
    # 한 글자씩 교차로 result에 추가
    if i < s1_len:
        result += s1[i]
    
    if i < s2_len:
        result += s2[i]

# 출력
print(result)