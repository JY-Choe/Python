# for + if/elif/else + 카운팅 변수를 사용하세요.
positive = 0
negative = 0
zero = 0

# 수도코드: 숫자 입력 받기 / 받은 수에서 양수, 음수, 0 찾기 / 찾은 수만큼 카운트 해서 출력

# 10회 반복하기
for _ in range(10):
    # 숫자 입력 받기
    num = int(input())
    
    # 양수라면 positive 1 추가
    if num > 0:
        positive += 1

    # 음수라면 negative 1 추가
    elif num < 0:
        negative += 1

    # 이라면 zero 1 추가
    else:
        zero += 1

# 출력
print(f"양수: {positive}개")    # 양수 출력
print(f"음수: {negative}개")    # 음수 출력
print(f"0: {zero}개")   # 0 출력