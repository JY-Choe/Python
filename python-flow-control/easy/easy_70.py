# 끝값은 포함되지 않는 점에 유의해 for 반복문을 작성하세요.
start = int(input())
stop = int(input())
step = int(input())

# 입력 받은 start, stop, step을 반복문을 이용하여 출력
for index in range(start, stop, step):
    print(index,end=" ")