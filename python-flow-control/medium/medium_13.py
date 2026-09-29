# 공백을 먼저 (n-i)개 출력한 뒤 별을 i개 출력하세요.
n = int(input())

# 입력받은 수만큼 "*" 출력 / 공백 포함
for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)