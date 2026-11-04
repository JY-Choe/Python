# 각 학생 점수 입력 후 target 점수를 고르고 더 높은 수 세기
print("=== 5명의 점수 입력 ===")
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
target = int(input())

# 석차 초기화
count = 0

# 입력받은 점수 리스트로 만들기
score = [s1, s2, s3, s4, s5]

for i in score:
    # 석차 확인
    if score[target - 1] < i:
        count += 1

# 출력
print(f"{target}번 학생 점수: {score[target-1]}")
print(f"석차: {count + 1}등")