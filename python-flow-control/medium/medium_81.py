# 좌석번호를 열(A~J)과 번호(1~10)로 변환하세요
seat = int(input())

# 한 열에 10자리, 총 10열(A~J)
# 좌석 1 ~ 10 : A열 1 ~ 10번
# 좌석 11 ~ 20 : B열 1 ~ 10번
if seat < 1 or seat > 100:
    result = "잘못된 좌석번호입니다."

else:
    row = "ABCDEFGHIJ"[(seat - 1) // 10]  # 열 문자 계산
    num = (seat - 1) % 10 + 1             # 열 내 번호 계산
    result = f"좌석 {seat} → {row}열 {num}번"
    
# 출력
print(result)