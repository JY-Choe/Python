# 인덱스 0과 len-1만 원래 글자, 나머지는 *
text = input()
result = ""

# 첫번째와 마지막을 제외한 나머지는 "*"로 출력
for i in range(len(text)):  
    # 0과 len - 1만 원래 글자
    if i == 0 or i == (len(text) - 1):
        result += text[i]
        
    # 나머지는 *로 출력
    else:
        result += "*"

# 출력
print("마스킹 결과:", result)