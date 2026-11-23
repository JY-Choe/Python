# 플레이어 HP와 몬스터 HP를 입력받아 턴제 전투를 시뮬레이션하세요.
player_hp = int(input())
monster_hp = int(input())

# turn 변수 초기화
turn = 1

# 시작
print("=== RPG 전투 시작! ===")
print(f"플레이어 HP: {player_hp} | 몬스터 HP: {monster_hp}")
print()

# 무한 반복
while True:
    # 공격력 공식
    p_damage = 15 + (turn * 7 + 3) % 11
    m_damage = 10 + (turn * 13 + 5) % 11

    # 매턴
    print(f"--- {turn}턴 ---")
    
    # 플레이어 먼저 공격
    monster_hp -= p_damage
    print(f"플레이어 공격! 데미지: {p_damage} | 몬스터 HP: {monster_hp}")
    
    # 몬스터가 살아 있으면 몬스터 공격
    if monster_hp > 0:
        player_hp -= m_damage
        print(f"몬스터 공격! 데미지: {m_damage} | 플레이어 HP: {player_hp}")
        print()
    
    # 몬스터가 죽었다면
    if monster_hp <= 0:
        print()
        print(f"플레이어 승리! ({turn}턴 만에 승리)")
        break

    # 플레이어가 죽었다면
    elif player_hp <= 0:
        print("몬스터 승리... (플레이어 패배)")
        break

    # turn 값 1추가
    turn += 1