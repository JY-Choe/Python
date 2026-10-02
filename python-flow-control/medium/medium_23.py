# 먼저 등급을 판별한 뒤 수료 여부를 판단하세요.
score = int(input())
attendance = int(input())

# 점수가 90점 이상: A
if score >= 90:
    rating = "A"
    
# 점수가 80점 이상: B
elif score >= 80:
    rating = "B"

# 점수가 70점 이상: C
elif score >= 70:
    rating = "C"

# 점수가 60점 이상: D
elif score >= 60:
    rating = "D"

#  점수가 60점 미만: F
else:
    rating = "F"


# 등급이 F이면 "미수료 - 성적 미달 (60점 이상 필요)"
if rating == "F":
    comment = "미수료 - 성적 미달 (60점 이상 필요)"

# 출석률이 80 이상이면 "수료를 축하합니다!"
elif attendance >= 80:
    comment = "수료를 축하합니다!"

# 출석률이 80 이하이면 "미수료 - 출석률 부족 (80% 이상 필요)"
else:
    comment = "미수료 - 출석률 부족 (80% 이상 필요)"

# 등급 출력
print(f"등급: {rating}")

# comment 출력
print(comment)