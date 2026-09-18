# 바깥 if는 파일명, 안쪽 if는 확장자 기준으로 작성하세요.
filename = input()
extension = input()

# 파일명이 있다면
if filename:
    # txt파일이면 "텍스트 파일 저장"
    if extension == "txt":
        print("텍스트 파일 저장")

    # 그렇지 않으면 "지원되지 않은 형식"
    else:
        print("지원되지 않는 형식")

# 파일명이 없다면
else:
    print("파일명을 입력하세요")