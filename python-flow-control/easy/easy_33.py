# 1부터 20까지 반복하며 짝수(i % 2 == 0)만 합계에 누적하세요.
total = 0

for num in range(1, 21):
    if num % 2 == 0:
        total += num
# 출력
print(f"1~20 짝수 합계: {total}")
