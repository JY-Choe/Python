# 층수를 입력받아 각 층의 요금과 누적 요금을 출력하세요.
n = int(input())

# price 초기화
price = 0

# total 초기화
total = 0

# 입력받은 층만큼 반복
for i in range(1, n + 1):
    # 층이 하나씩 오를때마다 100 원 추가
    price = 100 * i
    # 누적 값 구하기
    total += price
    # n층: n00원 (누적: x원)출력
    print(f"{i}층: {price}원 (누적: {total}원)")