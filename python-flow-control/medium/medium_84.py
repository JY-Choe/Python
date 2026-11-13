# for문과 isupper(), islower(), isdigit()를 사용하세요.
s = input()
upper = 0
lower = 0
digit = 0
other = 0

# 각 문자를 순회하며 종류별 카운트
for char in s:
    if char.isupper():
        upper += 1

    elif char.islower():
        lower += 1

    elif char.isdigit():
        digit += 1
        
    else:   # 기타 문자 카운트
        other += 1

# 출력
print(f"대문자: {upper}")
print(f"소문자: {lower}")
print(f"숫자: {digit}")
print(f"기타: {other}")