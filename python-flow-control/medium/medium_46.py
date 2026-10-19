# 1부터 num-1까지의 약수의 합을 구해 비교
num = int(input())
total = 0

# 수도코드: 입력 받은 숫자의 약수 구하기(입력 받은 숫자는 제외) / 약수를 구한 후 약수의 합을 구함 / 출력

for i in range(1, num):     # 입력 받은 숫자만큼 반복(입력 받은 숫자 제외)
    if num % i == 0:    # 입력 받은 수의 약수 구하기
        total += i      # 약수의 합

# 약수의 합과 입력 받은 수가 같다면 / "완전수입니다!"
if total == num:
    comment = "완전수입니다!"
    
# 약수의 합과 입력 받은 수가 같지 않다면 / "완전수가 아닙니다."
else:
    comment = "완전수가 아닙니다."

# 출력
print(f"{num}의 약수의 합: {total}")
print(f"{num}은(는) {comment}")