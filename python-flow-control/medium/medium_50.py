# 모드에 따라 변환 공식을 선택하고 최고/최저 갱신
mode = int(input())
n = int(input())
max_temp = -9999
min_temp = 9999

# 입력 받은 mode에 따라 온도 선택
if mode == 1:
    unit = '°F'

elif mode == 2:
    unit = '°C'

# 입력 받은 횟수만큼 반복
for _ in range(n):
        
    # 숫자 입력 받기
    num = int(input())
    
    # 입력 받은 mode 선택
    if mode == 1:
        # 변환 식
        temp = num * 9 / 5 + 32
        
    elif mode == 2:
        # 변환 식
        temp = (num - 32) * 5 / 9 
    
    # 변환 결과 출력
    print(f"변환 결과: {temp}{unit}")
    
    # 가장 큰 결과 값 찾기
    if temp > max_temp:
        max_temp = temp
    # 가장 작은 결과 값 찾기
    if temp < min_temp:
        min_temp = temp

# 출력
print("최고 변환 온도:", max_temp)
print("최저 변환 온도:", min_temp)