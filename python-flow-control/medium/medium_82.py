# 문자열을 입력받아 같은 문자가 연속으로 가장 많이 반복된 횟수를 출력하세요.
s = input()

# 변수 초기화
current_count = 1
max_count = 1

# 문자 길이만큼 반복
for i in range(len(s) - 1):
    # index값을 사용하여 연속으로 가장 많이 반복된 횟수 추적
    if s[i] == s[i + 1]:
        current_count += 1
        
    # 반복되지 않는다면 
    else:
        # 최대 값 찾기
        max_count = max(max_count, current_count)
        # 변수 초기화
        current_count = 1

# 최대 값 찾기
max_count = max(max_count, current_count)

# 출력
print(max_count)