import random
import time

HP = 100
HPregular = 100
ATK = 20
ATKregular = 20
LV = 1
EXP = 0
GOLD = 0
CRI = 0
MP = 100
MPregular = 100
SP = 0
SKATK = 40

MHP = 100
MATK = 0
MTYPE = 0

Turn = 1
DChoose = 0
UChoose = 0
VChoose = 0
SChoose = 0
TChoose = 0
QChoose = 0
QUE = 0
Chestplate = 1
Sword = 1
Ring = 1
EVE = 0
KT = 0
DIF = 0
WT = 0
DT = 0

def MAT():
    global HP, Turn, MATK
    HP -= MATK
    Turn += 1
    print(f"몬스터가 공격했습니다. 당신의 남은 HP:{HP}\n")
    time.sleep(1)

def PAT():
    global MHP, ATK, CRI
    CRI = random.randint(1,10)
    if CRI == 10:
        MHP -= ATK*3
        print(f"당신은 몬스터를 아주 강하게 공격했습니다! 몬스터의 남은 HP:{MHP}\n")
    elif CRI == 1:
        print(f"당신은 최선을 다했지만, 몬스터는 가볍게 피했습니다. 몬스터의 남은 HP:{MHP}\n")
    else:
        MHP -= ATK
        print(f"당신은 몬스터를 공격했습니다. 몬스터의 남은 HP:{MHP}\n")

def PHEAL():
    global HP, HPregular
    HP += 40
    if HP > HPregular:
        HP = HPregular
    print(f"당신은 회복했습니다. 당신의 남은 HP:{HP}\n")

def SKILL():
    global MP, MHP, SKATK
    if MP < 40:
        print("당신의 MP가 부족합니다.")
        return
    MP -= 40
    MHP -= SKATK
    print(f"당신은 스킬 소드 스핀을 사용했습니다. 몬스터의 남은 HP:{MHP}, 당신의 잔여 MP:{MP}\n")

def EVENT():
    global EVE, ATK, HP, MP, HPregular
    EVE = random.randint(1,3)
    if EVE == 1:
        print("당신은 개미가 되었습니다! 공격력과 HP,MP가 모두 1이 됩니다.")
        ATK = 1
        HP = 1
        MP = 1
    elif EVE == 2:
        print("공격력이 2배가 되었습니다!")
        ATK += ATK
    elif EVE == 3:
        print("HP가 완전히 회복되었습니다!")
        HP = HPregular

def RESIGN():
    global LV, EXP, GOLD, HP, DT, SP
    print("기권으로 인해 패배했습니다.\n")
    DT += 1
    if LV == 1 and EXP == 0 and GOLD == 0:
        print(f"LV = 1, 잔여 EXP = 0, 잔여 GOLD = 0\n")
    else:
        EXP -= 10
        GOLD -= 5
        SP += 1
        if GOLD < 0:
            GOLD = 0
        if EXP < 0 and LV > 1:
            EXP = 20 + EXP
            LV -= 1
        elif EXP < 0 and LV < 2:
            EXP = 0
        print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n")

def DEFEAT():
    global LV, EXP, GOLD, HP, DT, SP
    print("HP 소진으로 인해 패배했습니다.\n")
    DT += 1
    if LV == 1 and EXP == 0 and GOLD == 0:
        print(f"LV = 1, 잔여 EXP = 0, 잔여 GOLD = 0\n")
    else:
        EXP -= 10
        GOLD -= 5
        SP += 1
        if GOLD < 0:
            GOLD = 0
        if EXP < 0 and LV > 1:
            EXP = 100 + EXP
            LV -= 1
        elif EXP < 0 and LV < 2:
            EXP = 0
        print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n")

def WIN():
    global LV, EXP, GOLD, HP, ATKregular, HPregular, MPregular, WT, SP
    print("축하합니다. 승리하셨습니다.\n")
    WT += 1
    EXP += 10
    GOLD += 5
    SP += 3
    if EXP > 30:
        EXP -= 30
        LV += 1
        ATKregular += 10
        HPregular += 10
        MPregular += 10
        SP += 5
    print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n")

def WINEASY():
    global LV, EXP, GOLD, HP, ATKregular, HPregular, MPregular, WT, SP
    print("축하합니다. 승리하셨습니다.\n")
    WT += 1
    EXP += 1
    GOLD += 1
    SP += 1
    if EXP > 30:
        EXP -= 30
        LV += 1
        ATKregular += 10
        HPregular += 10
        MPregular += 10
        SP += 5
    print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n")

def WINHARD():
    global LV, EXP, GOLD, HP, ATKregular, HPregular, MPregular, WT, SP
    print("축하합니다. 승리하셨습니다.\n")
    WT += 1
    EXP += 500
    GOLD += 250
    SP += 100
    if EXP > 30:
        EXP -= 30
        LV += 1
        ATKregular += 10
        HPregular += 10
        MPregular += 10
        SP += 5
    print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n")

def SHOP():
    global GOLD, SChoose, HPregular, ATKregular, Sword, Chestplate, Ring, MPregular

    while True:
        items = {
            1: {"name": "나무막대기", "price": 1, "stat": "ATK", "stock": Sword},
            2: {"name": "나무 상자", "price": 1, "stat": "HP", "stock": Chestplate},
            3: {"name": "고무줄", "price": 1, "stat": "MP", "stock": Ring},
            4: {"name": "나가기"}
        }

        print("\n상점입니다. 무엇을 구매하시겠습니까?")
        for key, item in items.items():
            if key == 4:
                print(f"{key}. {item['name']}")
            else:
                stock_status = "(매진)" if item["stock"] == 0 else f"({item['price']}G)"
                print(f"{key}. {item['name']} {stock_status}")

        SChoose = int(input())

        if SChoose == 4:
            break

        if SChoose not in [1, 2, 3]:
            print("잘못된 선택입니다.")
            continue

        item = items[SChoose]

        if item["stock"] == 0:
            print("매진되었습니다.")
            continue

        if GOLD < item["price"]:
            print("골드가 부족합니다.")
            continue

        GOLD -= item["price"]
        print(f"{item['name']} 구매 완료!")

        if item["stat"] == "ATK":
            ATKregular += 5
            Sword = 0
        elif item["stat"] == "HP":
            HPregular += 5
            Chestplate = 0
        elif item["stat"] == "MP":
            MPregular += 5
            Ring = 0


def EASY():
    global HP, HPregular, MATK, MHP, MTYPE, DChoose, Turn
    HP = HPregular
    MHP = 1
    MATK = 7
    Turn = 1
    print("당신은 개미를 만났습니다. 개미는 너무 약합니다!")
    while HP > 0 and MHP > 0:
        print(f"{Turn}번째 턴.")
        DChoose = int(input("1.공격 2.회복 3.스킬 4.특별 이벤트 5.기권\n"))
        if DChoose == 1:
            PAT()
        elif DChoose == 2:
            PHEAL()
        elif DChoose == 3:
            SKILL()
        elif DChoose == 4:
            EVENT()
        elif DChoose == 5:
            break
        else:
            print("잘못된 입력입니다.")
        time.sleep(1)
        MAT()
    if DChoose == 5:
        RESIGN()
    elif HP <= 0:
        DEFEAT()
    elif MHP <= 0:
        WINEASY()

# 여기서부터 MEDIUM, HARD, TRAIN, QUEST, DUNGEON, PLAY도 같은 식으로 이어서 구현 가능.
def MEDIUM():
    global HP, HPregular, MATK, MHP, MTYPE, DChoose, Turn
    MTYPE = random.randint(1,5)
    if MTYPE == 1:
        MHP = 30
        MATK = 7
        print("슬라임 등장! 약하지만 빠릅니다.")
    elif MTYPE == 2:
        MHP = 150
        MATK = 10
        print("오크 등장! 체력 많지만 공격 약함.")
    elif MTYPE == 3:
        MHP = 80
        MATK = 20
        print("좀비 등장! 균형 잡힌 적.")
    elif MTYPE == 4:
        MHP = 50
        MATK = 40
        print("엘프 등장! 강력하지만 체력 적음.")
    elif MTYPE == 5:
        MHP = 1
        MATK = 7
        print("개미 등장! 너무 약함.")
    HP = HPregular
    Turn = 1
    while HP > 0 and MHP > 0:
        print(f"{Turn}번째 턴.")
        DChoose = int(input("1.공격 2.회복 3.스킬 4.특별 이벤트 5.기권\n"))
        if DChoose == 1:
            PAT()
        elif DChoose == 2:
            PHEAL()
        elif DChoose == 3:
            SKILL()
        elif DChoose == 4:
            EVENT()
        elif DChoose == 5:
            break
        else:
            print("잘못된 입력입니다.")
        time.sleep(1)
        MAT()
    if DChoose == 5:
        RESIGN()
    elif HP <= 0:
        DEFEAT()
    elif MHP <= 0:
        WIN()

def HARD():
    global HP, HPregular, MATK, MHP, MTYPE, DChoose, Turn
    MTYPE = random.randint(1,5)
    if MTYPE == 1:
        MHP = 100
        MATK = 70
        print("슈퍼슬라임 등장! 강력함.")
    elif MTYPE == 2:
        MHP = 150
        MATK = 100
        print("슈퍼오크 등장! 강력함.")
    elif MTYPE == 3:
        MHP = 150
        MATK = 80
        print("슈퍼좀비 등장! 강력함.")
    elif MTYPE == 4:
        MHP = 120
        MATK = 120
        print("슈퍼엘프 등장! 강력함.")
    elif MTYPE == 5:
        MHP = 200
        MATK = 150
        print("슈퍼개미 등장! 최강!")
    HP = HPregular
    Turn = 1
    while HP > 0 and MHP > 0:
        print(f"{Turn}번째 턴.")
        DChoose = int(input("1.공격 2.회복 3.스킬 4.특별 이벤트 5.기권\n"))
        if DChoose == 1:
            PAT()
        elif DChoose == 2:
            PHEAL()
        elif DChoose == 3:
            SKILL()
        elif DChoose == 4:
            EVENT()
        elif DChoose == 5:
            break
        else:
            print("잘못된 입력입니다.")
        time.sleep(1)
        MAT()
    if DChoose == 5:
        RESIGN()
    elif HP <= 0:
        DEFEAT()
    elif MHP <= 0:
        WINHARD()

def TRAIN():
    global SKATK, SP, TChoose
    while True:
        TChoose = int(input(f"스킬 훈련하시겠습니까? 잔여 SP:{SP}\n1.훈련 2.나간다\n"))
        if TChoose == 1:
            if SP < 1:
                print("SP가 부족합니다.")
            else:
                SP -= 1
                SKATK += 1
                print(f"스킬 훈련 완료! 현재 스킬 공격력:{SKATK}, 잔여 SP:{SP}")
        elif TChoose == 2:
            break
        else:
            print("잘못된 입력입니다.")

def QUEST():
    global KT, QChoose, QUE, GOLD, EXP
    while True:
        QChoose = int(input("마을 이장의 집\n1.말 걸기 2.나가기\n"))
        if QChoose == 1:
            if QUE == 0:
                print("마을이장: 몬스터 5마리만 잡아주게나.")
                QUE = 1
            elif QUE == 1:
                if KT >= 5:
                    print("마을이장: 고맙네. 100G와 50EXP를 주겠네.")
                    GOLD += 100
                    EXP += 50
                    QUE = 2
                else:
                    print("마을이장: 몬스터를 다 잡고 말을 걸어주게나.")
        elif QChoose == 2:
            break
        else:
            print("잘못된 입력입니다.")

def DUNGEON():
    global DIF
    DIF = int(input("던전 난이도 설정\n1.쉬움 2.보통 3.어려움 4.나가기\n"))
    if DIF == 1:
        EASY()
    elif DIF == 2:
        MEDIUM()
    elif DIF == 3:
        HARD()

def STAT():
    print(f"승리:{WT}, 패배:{DT}")

def PLAY():
    global VChoose, ATK, ATKregular
    while True:
        ATK = ATKregular
        VChoose = int(input("마을입니다. 어디로?\n1.상점 2.던전 3.훈련소 4.마을 이장 5.전적 6.종료\n"))
        if VChoose == 1:
            SHOP()
        elif VChoose == 2:
            DUNGEON()
        elif VChoose == 3:
            TRAIN()
        elif VChoose == 4:
            QUEST()
        elif VChoose == 5:
            STAT()
        elif VChoose == 6:
            print("게임 종료")
            break
        else:
            print("잘못된 입력입니다.")

PLAY()
