# //(몫)과 %(나머지)를 사용해 큰 동전부터 차례대로 계산하세요.
amount = int(input())

# 입력받은 금액을 500원 / 100원 / 50원 / 10원 동전으로 최소 개수 변환
# 입력 받은 금액을 500원으로 나누기
coin_500 = amount // 500 # 몫
remainder = amount % 500 # 나머지

# 500원을 나눈 금액을 100원으로 나누기
coin_100 = remainder // 100 # 몫
remainder = remainder % 100 # 나머지

# 100원으로 나눈 금액을 50원으로 나누기
coin_50 = remainder // 50 # 몫
remainder = remainder % 50 # 나머지

# 50원으로 나눈 금액을 10원으로 나누기
coin_10 = remainder // 10 # 몫

# 출력
print(f"{amount}원 → 동전 변환:")
print(f"500원: {coin_500}개")
print(f"100원: {coin_100}개")
print(f"50원: {coin_50}개")
print(f"10원: {coin_10}개")
print(f"총 동전 수: {coin_500 + coin_100 + coin_50 + coin_10}개")