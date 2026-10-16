# for + if/elif를 사용하세요.
n = int(input())

# 별 개수 초기화
star = 0

# 수도 코드: 입력 받은 수만큼 반복 / 점수에 따라 별(★) 개수를 나눔 / 출력
for index, _ in enumerate(range(n),1):  # range를 사용하지 않으면 반복 x
    score = int(input())    # 점수 입력 받기
    # 90점 이상
    if score >= 90:
        star = 5
    
    # 80점 이상
    elif score >= 80:
        star = 4
   
    # 70점 이상
    elif score >= 70:
        star = 3
    
    # 60점 이상
    elif score >= 60:
        star = 2
    
    # 그 외 나머지
    else:
        star = 1

    # 출력
    print(f"{index}번 학생:","★" * star)