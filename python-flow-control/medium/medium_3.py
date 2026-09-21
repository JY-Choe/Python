# for i in range(1, 21): if i % 3 == 0: continue; print(i)
# 1부터 20까지의 수 중 3의 배수는 건너뛰고 나머지를 한 줄에 하나씩 출력하시오.
for i in range(1,21):
    if i % 3 == 0:
        continue
    
    # 출력
    print(i)