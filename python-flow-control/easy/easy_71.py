# 한 줄에 이어 출력하려면 번호 카운터 변수를 따로 두고, 한 항목 출력 후 공백을 붙이세요.
text = input()

# text를 각 글자 앞에 1부터 시작하는 번호를 붙여 출력
for index, char in enumerate(text, 1):
    print(f"{index}.{char}",end=" ")