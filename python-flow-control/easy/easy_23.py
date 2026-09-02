# AB형을 A보다 먼저 검사해야 합니다.
blood = input()

blood_types = {
    "AB": "이성적이고 독창적인 성격",            # AB형: 이성적이고 독창적인 성격
    "A": "꼼꼼하고 신중한 성격",                # A형: 꼼꼼하고 신중한 성격
    "B": "자유롭고 창의적인 성격",              # B형: 자유롭고 창의적인 성격
    "O": "사교적이고 리더십이 강한 성격",       # O형: 사교적이고 리더십이 강한 성격
}

if blood in blood_types:
    print(f"혈액형: {blood}형")
    print(f"성격: {blood_types[blood]}")
    
else:
    print("잘못된 입력입니다.")  # 그 외 입력은 잘못된 입력입니다.