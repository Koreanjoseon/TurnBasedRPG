#import 하는 곳
import random
import time

#플레이어 설정
HP = 100 #플레이어 HP 설정, 기본값 100
HPregular = 100 #플레이어 체력 증가용, 기본값 100
ATK = 20 #플레이어 공격력 설정, 기본값 20
ATKregular = 20 #플레이어 공격력 증가용, 기본값 20
LV = 1 #플레이어 레벨 설정, 기본값 1
EXP = 0 #플레이어 경험치 설정, 기본값 0
GOLD = 0 #플레이어 재화 설정, 기본값 0

#몬스터 설정
MHP = 100 #몬스터 HP 설정, 기본값 100
MHPregular = 100 #몬스터 체력 증가용, 기본값 100
MATK = 0 #몬스터 공격력 설정, 랜덤 돌릴거라 기본값 0

#기타 설정
Turn = 1 #턴 설정, 기본값은 1
DChoose = 0 #플레이어 선택(던전), 기본값은 0
VChoose = 0 #플레이어 선택(마을), 기본값은 0
SChoose = 0 #플레이어 선택(상점), 기본값은 0
Chestplate = 1 #상점에서 판매하는 갑옷, 기본값은 1
Sword = 1 #상점에서 판매하는 검, 기본값은 1

#함수 정의
def MAT(): #몬스터 공격 함수 정의, 1턴 소모
    global HP, Turn
    MATK = random.randint(18, 25)
    HP -= MATK
    Turn += 1
    print(f"몬스터가 공격했습니다. 당신의 남은 HP:{HP}\n")
    time.sleep(1)
def PAT(): #플레이어 공격 함수 정의
    global MHP
    MHP -= ATK
    print(f"당신은 몬스터를 공격했습니다. 몬스터의 남은 HP:{MHP}\n")
def PHEAL():
    global HP, HPregular
    HP += 40
    if HP > HPregular:
        HP = HPregular
    print(f"당신은 회복했습니다. 당신의 남은 HP:{HP}\n")
def RESIGN(): #기권패 함수 정의
    global LV, EXP, GOLD, HP
    print("기권으로 인해 패배했습니다.\n")
    if(LV == 1 and EXP == 0 and GOLD == 0):
        print(f"LV = 1, 잔여 EXP = 0, 잔여 GOLD = 0\n") #스탯
    else:
        EXP -= 10
        GOLD -= 5
        if(GOLD < 0):
            GOLD = 0
        if(EXP < 0 and LV > 1):
            EXP = 20 + EXP
            LV -= 1
        elif(EXP < 0 and LV < 2):
            EXP = 0
        print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n") #스탯
def DEFEAT(): #HP패 함수 정의
    global LV, EXP, GOLD, HP
    print("HP 소진으로 인해 패배했습니다.\n")
    if(LV == 1 and EXP == 0 and GOLD == 0):
        print(f"LV = 1, 잔여 EXP = 0, 잔여 GOLD = 0\n") #스탯
    else:
        EXP -= 10
        GOLD -= 5
        if(GOLD < 0):
            GOLD = 0
        if(EXP < 0 and LV > 1):
            EXP = 100 + EXP
            LV -= 1
        elif(EXP < 0 and LV < 2):
            EXP = 0
        print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n") #스탯
def WIN(): #승리 함수 정의
    global LV, EXP, GOLD, HP
    print("축하합니다. 승리하셨습니다.\n")
    EXP += 10
    GOLD += 5
    if(EXP > 100):
        EXP -= 100
        LV += 1
    print(f"LV = {LV}, 잔여 EXP = {EXP}, 잔여 GOLD = {GOLD}\n") #스탯
def SHOP():
    global GOLD, SChoose, HPregular, ATKregular, Sword, Chestplate
    
    items = {
        1: {"name": "나무막대기", "price": 1, "stat": "ATK", "stock": Sword},
        2: {"name": "나무 상자", "price": 1, "stat": "HP", "stock": Chestplate},
        3: {"name": "나가기"}
    }
    
    while True:
        print("\n상점입니다. 무엇을 구매하시겠습니까?")
        for key, item in items.items():
            if key == 3:
                print(f"{key}. {item['name']}")
            else:
                stock_status = "(매진)" if item["stock"] == 0 else f"({item['price']}G)"
                print(f"{key}. {item['name']} {stock_status}")
        
        SChoose = int(input())
        
        if SChoose == 3:
            break
        elif SChoose in [1,2]:
            item = items[SChoose]
            if item["stock"] == 0:
                print("매진되었습니다.")
            elif GOLD < item["price"]:
                print("골드가 부족합니다.")
            else:
                print(f"{item['name']} 구매 완료!")
                GOLD -= item["price"]
                if item["stat"] == "ATK":
                    ATKregular += 5
                    Sword = 0
                    items[1]["stock"] = 0
                elif item["stat"] == "HP":
                    HPregular += 5
                    Chestplate = 0
                    items[2]["stock"] = 0
        else:
            print("잘못된 선택입니다.")

def DUNGEON():
    global HP, MHP, MHPregular, HPregular, DChoose
    #전투 시작
    print("당신은 몬스터를 만났습니다.\n")
    HP = HPregular
    MHP = MHPregular
    while HP > 0 and MHP > 0:
        print(f"{Turn}번째 턴.")
        DChoose = int(input("\n무엇을 하시겠습니까?\n1.공격\n2.회복\n3.기권\n")) #플레이어 공격 휴식 기권 선택
        if(DChoose == 1):
            PAT()
        elif(DChoose == 2):
            PHEAL()
        elif(DChoose == 3):
            break
        else:
            print("잘못된 입력입니다. 턴이 넘어갑니다.\n") #턴 넘김
        time.sleep(1)
        MAT()

    #전투 끝
    MHPregular += 20
    if(DChoose == 3):
        RESIGN()
    elif(DChoose != 3 and HP <= 0):
        DEFEAT()
    elif(DChoose != 3 and MHP <= 0):
        WIN()
def PLAY():
    global VChoose, ATK, ATKregular
    while True:
        #게임 진행
        ATK = ATKregular
        VChoose = int(input("\n마을입니다. 어디로 가시겠습니까?\n1.상점\n2.던전\n3.게임 종료\n")) #선택
        if(VChoose == 1):
            SHOP()
        if(VChoose == 2):
            DUNGEON()
        if(VChoose == 3):
            print("게임을 종료합니다.")
            break
            
PLAY()
    
    



