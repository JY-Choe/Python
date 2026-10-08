# 각 감가율을 따로 계산한 뒤 합산하고 최저가를 체크하세요.
new_price = int(input())
year = int(input())
km = float(input())
accident = input()

# 감가 내역 출력
print("--- 감가 내역 ---")

# 연식 감가율
if year <= 3:
    year_discount = year * 10
elif year <= 7:
    year_discount = 3 * 10 + (year - 3) * 7
else:
    year_discount = 3 * 10 + 4 * 7 + (year - 7) * 5

# 감가 출력
print(f"연식 감가 ({year}년): {year_discount}%")

# 주행거리 감가율
if km <= 5:
    km_discount = 0
elif km <= 10:
    km_discount = 5
else:
    km_discount = 10

# 주행거리 출력
print(f"주행거리 감가: {km_discount}%")

# 사고 감가율
if accident.upper() == "Y":
    accident_discount = 15
else:
    accident_discount = 0

# 사고 감가 출력
print(f"사고 감가: {accident_discount}%")

# 총 감가율
total_discount = year_discount + km_discount + accident_discount

# 출력
print(f"총 감가율: {total_discount}%")

# 예상 중고차 가격
final_price = int(new_price * (1 - total_discount / 100))
min_price = int(new_price * 0.1)

# 최종가격이 최소보다 작으면 최소가격으로
if final_price < min_price:
    final_price = min_price

# 출력
print(f"예상 중고차 가격: {final_price}만원")