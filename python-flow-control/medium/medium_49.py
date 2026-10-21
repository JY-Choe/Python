# range(start, end+1)로 반복
start = int(input())
end = int(input())
total = 0
even_sum = 0

# 입력 받은 수까지의 반복
for num in range(start, end + 1):
    # 전체의 합
    total += num
    
    # 짝수 합계
    if num % 2 == 0:
        even_sum += num

# 출력
print("구간 합계:", total)
print("짝수 합계:", even_sum)