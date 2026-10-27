# 뒤집은 문자열과 원본을 비교
text = input()
reversed_text = ""

# 입력 받은 문자를 거꾸로 출력
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

# 앞뒤가 똑같다면 "회문입니다!" 출력
if text == reversed_text:
    print(f"{text}은(는) 회문입니다!")

# 그렇지 않다면 "회문이 아닙니다." 출력
else:
    print(f"{text}은(는) 회문이 아닙니다.")