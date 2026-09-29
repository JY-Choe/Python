# chr(65)는 'A', chr(65+1)은 'B'입니다.
n = int(input())

# 결과 값 문자열로 변경
result = ""

# 입력 받은 값 만큼 반복하여 알파벳을 추가
for index in range(n):
    result += chr(65 + index)
    print(result)