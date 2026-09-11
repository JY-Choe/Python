# 첫 입력을 먼저 받고 while num != 0 으로 반복하며 다음 입력을 받으세요.
total = 0
count = 0

# 숫자 입력받기
num = int(input())

# 입력한 숫자들의 평균 출력 / 0이 되면 종료
while num != 0:
    total += num
    count += 1
    num = int(input())

# 출력
if count == 0:
    print("입력한 숫자가 없습니다.")
    
else:
    # 평균 결과 값
    average = total / count
    print(f"평균: {average}")