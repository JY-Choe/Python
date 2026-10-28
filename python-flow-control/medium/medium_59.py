# 바깥 for는 각 글자, 안쪽 for는 n번 출력
text = input()
n = int(input())

# list 생성
result = []

# 글자 하나씩 처리
for char in text:
    # 하나씩 처리한 글자 n값만큼 반복
    result.append(char * n)

# 출력
print(''.join(result))