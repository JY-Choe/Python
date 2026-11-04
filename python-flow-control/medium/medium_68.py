# 위 수식 그대로, 플레이어 선공 → 몬스터 사망 확인 → 몬스터 공격 → 플레이어 사망 확인
player_hp = 100
monster_hp = 80
turn = 0

# 화면 출력
print("=== RPG 전투 시작! ===")
print("플레이어 HP:", player_hp, "| 몬스터 HP:", monster_hp)
print()

# 플래그 변수 초기화
player_win = False

# 플레이어의 hp가0이하 이면 종료
while player_hp > 0 and monster_hp > 0:

    # 매턴 마다 횟수 추가
    turn += 1
    print(f"--- {turn}턴 ---")
   
    # 플레이어 데미지 식
    p_damage = 15 + (turn * 7 + 3) % 11
    
    # 몬스터 데미지 식
    m_damage = 10 + (turn * 11 + 5) % 11
    
    # 플레이어 공격 먼저
    monster_hp -= p_damage
    print(f"플레이어 공격! 데미지: {p_damage} | 몬스터 HP: {monster_hp}")
    
    # 몬스터 공격
    if monster_hp > 0:
        player_hp -= m_damage
        print(f"몬스터 공격! 데미지: {m_damage} | 플레이어 HP: {player_hp}")
        print()
    
    # 몬스터의 hp가 0이하이면 즉시종료 
    else:
        player_win = True
        print()
        break
        
# 출력
if player_win and monster_hp <= 0:
    print(f"플레이어 승리! ({turn}턴 만에 승리)")