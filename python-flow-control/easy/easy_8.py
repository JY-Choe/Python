# %(나머지) 연산자와 if/else를 사용해 홀짝을 판별하세요.
num = int(input())

# 입력받은 값이 홀수 인지 짝수인지 판단
if num % 2 == 0:
    print(f"{num}은(는) 짝수입니다")
    
else:
    print(f"{num}은(는) 홀수입니다")