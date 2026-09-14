# 단가와 수량범위 N을 입력받아 가격표를 출력하세요.
price = int(input())
n = int(input())

# n값만큼 반복
for i in range(1, n + 1):
    
    # 단가 * 수량 범위
    print(i, "x", price, "=" ,(i * price))