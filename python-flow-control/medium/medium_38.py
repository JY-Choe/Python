# while True + break를 사용하세요.
total = 0
count = 0

# 수도 코드: 반복 실행 / 누적 합 구함 / 누적 합이 100 초과 이면 종료 / 출력
while True:
    # 숫자 입력 받기
    score = int(input())

    # 누적 합 구하기
    total += score

    # 입력 횟수
    count += 1

    # 누적 합이 100 초과이면 출력 후 break
    if total > 100:
        print("누적합이 100을 초과했습니다!")
        print(f"누적합: {total}")
        print(f"입력 횟수: {count}")
        break