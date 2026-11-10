# 합이 7인지, 더블인지 순서대로 확인
d1 = int(input())
d2 = int(input())

# 주사위 값 출력
print(f"주사위: {d1}, {d2}")

# 주사위 합이 7이면 "럭키세븐!"
total = d1 + d2

# 합이 7일 경우
if total == 7:
    print("럭키세븐!")

# 두값이 같으면 "더블!"
elif d1 == d2:
    print("더블!")

# 그 외 "합: x"
else:
    print(f"합: {total}")