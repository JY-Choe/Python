# 1부터 num까지 반복하며 나머지가 0이면 약수
num = int(input())
count = 0

# 수도 코드: 입력 받은 값까지 반복 / 약수 구하기 / 출력
for i in range(1, num + 1):
    if num % i == 0:    # 약수 구하는 공식
        count += 1  # 약수를 구하면 카운트 추가
        # 약수 출력
        print(i)

# 개수 출력
print("약수의 개수:", count)