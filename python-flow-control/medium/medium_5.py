# for i in range(len(text)): 조건 만족 시 출력 후 break. found 플래그로 미발견 처리.
text = "hello python"
target = "p"

# 변수 초기화
result = 0

# 문자열에서 p를 찾는다
for result, found in enumerate(text):
    if found == target:
        print(f"'{target}'을(를) {result}번째 위치에서 찾았습니다!")
        break   

# 그 외
else:
    print("찾지 못했습니다")