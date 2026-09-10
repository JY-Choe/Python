# 원본 값을 따로 보관하고, while num > 0: num //= 10; count += 1 로 자릿수를 세세요.
num = int(input())

# 변수 초기화
count = 0

# 원본 값 보존
original_num = num

# 양의 정수를 입력받아 몇 자리 수인지 출력
while num > 0:
    num //= 10
    count += 1

print(f"{original_num}은(는) {count}자리 수입니다.")