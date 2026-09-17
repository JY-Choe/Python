# for문으로 한 글자씩 생성하세요.
n = int(input())

# 변수 초기화
alpha_count = 0  
num_count = 0    
result = ""

# 입력 받은 수만큼 반복
for i in range(1, n + 1):
    # 홀수 자리 출력: a부터 순서대로, z를 넘으면 다시 a부터
    if i % 2 != 0:
        result += chr(ord('a') + alpha_count % 26)  # 모듈러로 z→a 순환 처리
        alpha_count += 1

    # 짝수 자리 출력: 1부터 순서대로, 9를 넘으면 다시 0부터
    else:
        # 가장 명확한 방식
        digits = [str(d) for d in range(1, 10)] + ['0']
        result += digits[num_count % 10]
        num_count += 1

# 출력
print(result)