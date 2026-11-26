# 정수 나눗셈(//)을 사용해야 예시 값과 정확히 일치합니다. 연도를 세는 변수 + 두 종료 조건의 순서를 결정하세요.
principal = int(input())
annual_rate = int(input())
target_amount = int(input())

# 변수 별도 사용
asset = principal

# 1년차 ~ 50년차 순서대로 처리
for year in range(1, 51):  
    # 1년씩 자산을 갱신하며 목표 도달 여부 확인
    asset = asset + (asset * annual_rate) // 100

    # 목표 도달 후 break
    if asset >= target_amount:  
        print(f"{year}년 차에 목표 도달 (자산: {asset}만원)")
        break

# 50년 초과 시 break
else:    
    print("50년 안에 도달 불가")