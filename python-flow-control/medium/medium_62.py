# 문제마다 출력 후 input, 채점, 점수 누적
score = 0

# 리스트 작성
questions = [
    (1, 12, 8, 20),
    (2, 35, 17, 52),
    (3, 99, 1, 100),
    (4, 46, 27, 73),
    (5, 58, 34, 92),
]

# 문제 작성 / 정답 확인
for k, a, b, result in questions:
    
    print(f"문제 {k}: {a} + {b} = ?")
    answer = int(input())   # 답 입력 받음

    if result == answer:
        print("정답!")
        score += 20

    else:
        print(f"오답! 정답은 {result}입니다")

# 최종 점수
print("=== 최종 점수:", score, "/ 100 ===")