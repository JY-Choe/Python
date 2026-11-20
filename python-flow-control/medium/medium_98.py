# 구간별 개수를 세고, 0이 아닌 구간만 출력하세요.
n = int(input())

# list 생성 및 초기화
section_list = ["0~9", "10~19", "20~29", "30~39", "40~49", "50~59", "60~69", "70~79", "80~89", "90~100"]
count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# n값 만큼 반복
for _ in range(n):
    # 입력 받기
    score =  int(input())
    
    # section 위치 구하기
    share = score // 10
    if share == 10:
        share = 9
    
    # count_list 값 추가
    count_list[share] += 1

# 전체 순회
for i in range(10):
    # count_list 값이 0보다 크면 출력
    if count_list[i] > 0:
        print(f"{section_list[i]}: {(count_list[i] * '#')}")