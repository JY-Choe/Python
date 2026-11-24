# range는 음수 step을 지원합니다. 1 미만으로 내려가지 않도록 종료값을 설정하세요.
n = int(input())
k = int(input())

# list 생성
num_list = []

# 시작값 N값에서 K만큼 감소시키며 한 줄에 출력
for num in range(n, 0 ,-k):
    num_list.append(num)

# 출력
print(*num_list)
print("발사!")