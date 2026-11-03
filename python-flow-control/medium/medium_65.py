# 위 규칙을 그대로 구현
seed = int(input())

# 로또 번호 생성
n1 = (seed * 7 + 3) % 45 + 1

n2 = (n1 * 13 + 11) % 45 + 1
for _ in range(1):
    if n2 == n1:
        n2 = n2 % 45 + 1
    else:
        break

n3 = (n2 * 17 + 7) % 45 + 1
for _ in range(2):
    if n3 == n2 or n3 == n1:
        n3 = n3 % 45 + 1
    else:
        break

n4 = (n3 * 23 + 5) % 45 + 1
for _ in range(2):
    if n4 == n3 or n4 == n2 or n4 == n1:
        n4 = n4 % 45 + 1
    else:
        break

n5 = (n4 * 29 + 13) % 45 + 1
for _ in range(2):
    if n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
        n5 = n5 % 45 + 1
    else:
        break
        
n6 = (n5 * 31 + 17) % 45 + 1
for _ in range(2):
    if n6 == n5 or n6 == n4 or n6 == n3 or n6 == n2 or n6 == n1:
        n6 = n6 % 45 + 1
    else:
        break

# 출력
print("=== 로또 번호 ===")
print(f"번호 1: {n1}\n번호 2: {n2}\n번호 3: {n3}\n번호 4: {n4}\n번호 5: {n5}\n번호 6: {n6}\n행운을 빕니다!")