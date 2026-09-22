# for i in range(5): num = int(input()); if num % 2 != 0: print("홀수는 건너뜁니다"); continue; total += num
total = 0

# 5회 반복하는 동안 입력받은 수 중 홀수를 찾아 건너뛰기
for i in range(5):
    # 입력 받기
    num = int(input())

    # 홀수를 찾아 건너뛰기
    if num % 2 != 0:
        print("홀수는 건너뜁니다")
        continue    # 홀수를 찾은 후 계속 실행 

    # 짝수의 합
    total += num

# 출력
print("짝수 합계:", total)