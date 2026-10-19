# 10번 반복하며 양수/음수/0 분류
pos_sum = 0
neg_sum = 0
zero_count = 0

# 10번 반복 받기
for _ in range(10):
    
    # 숫자 입력 받기
    num = int(input())
    
    # 양수이면
    if num > 0:
        pos_sum += num
    
    # 음수이면
    elif num < 0:
        neg_sum += num
   
    # 0이면
    else:
        zero_count += 1

# 출력
print("양수의 합:", pos_sum)
print("음수의 합:", neg_sum)
print("0의 개수:", zero_count)