# "예"로 답한 재료만 이어 붙여 "나의 파스타: ..." 형식으로 출력하세요.
add_cheese = input()
add_bacon = input()
add_shrimp = input()
pasta = "파스타"

# 결과 값 초기화
result = ""

# 결과값에 pasta 대입
result = pasta

# 예로 답한 재료를 추가
if add_cheese == "예":
    result += " + 치즈"

if add_bacon == "예":
    result += " + 베이컨"

if add_shrimp == "예":
    result += " + 새우"

# 최종 결과 값 출력
print(f"나의 {pasta}: {result}")