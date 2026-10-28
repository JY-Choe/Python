# 바깥 for는 선택, 안쪽 for는 개수 세기
text = input()

# 입력 받은 문자 하나씩 출력
for char in text:
    # 변수 초기화
    count = 0

    # 입력 받은 문자 하나씩 출력
    for each in text:
    
        # 해당 글자가 몇번 나오는지 확인
        if char == each:
            count += 1
    
    # 출력
    print(f"{char}: {count}개")