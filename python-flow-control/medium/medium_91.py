# 10진법 정수를 8진법으로 변환하여 출력하세요. (oct() 사용 금지)
n = int(input())

# list 생성
remainder_list = []

# n값이 0보다 크면 계속 반복
while n > 0:
    # 나머지 값 구하기
    remainder = n % 8
    
    # list에 추가
    remainder_list.append(str(remainder))
    
    # 값 변경
    n //= 8

# 출력
print(''.join(remainder_list[::-1]))