# 구간 내 소수를 찾아 출력하세요.
start = int(input())
end = int(input())

# list 생성
prime_list = []

# start 값에서 end 값까지 반복
for i in range(start, end + 1):
    if i < 2:
        continue  # 2 미만은 소수가 아님

    # 소수 값 찾기
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break  

    # 찾은 소수 list에 추가
    if is_prime:
        prime_list.append(i)

# 출력
print(*prime_list)