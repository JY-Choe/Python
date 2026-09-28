# print(j, end="")을 사용해 줄바꿈 없이 이어서 출력하세요.
n = int(input())

# j값을 문자열로 초기화
j = ""

# 입력받은 수만큼 반복
for num in range(1, n + 1):
    j += str(num)
    # 출력 
    print(j)