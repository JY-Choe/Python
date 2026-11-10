# 사이즈별 단가를 정하고, 3판 이상이면 10% 할인
size = input()
qty = int(input())

# 가격 설정
s_price = 8000
m_price = 12000
l_price = 15000

# 할인 값 설정
discount = 0.9

# 사이즈별 단가 / 가격
if size == "S":
    if qty >= 3:
        price = int(s_price * qty * discount)
    else:
        price = s_price * qty

elif size == "M":
    if qty >= 3:
        price = int(m_price * qty * discount)
    else:
        price = m_price * qty

elif size == "L":
    if qty >= 3:
        price = int(l_price * qty * discount)
    else:
        price = l_price * qty

# 출력
print(f"사이즈: {size} | 수량: {qty}판")
print(f"총액: {price}원")

# 3판이상 시 할인표기
if qty >= 3:
    print("(10% 할인 적용)")