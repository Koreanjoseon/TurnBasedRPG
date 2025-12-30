#import 하는 곳
import random
import time

#플레이어 설정
HP = 100 #플레이어 HP 설정
ATK = 20 #플레이어 공격력 설정

#몬스터 설정
MHP = 100 #몬스터 HP 설정
MATK = 0 #몬스터 공격력 설정, 랜덤 돌릴거라 기본값 0

#기타 설정
Turn = 1 #턴 설정, 기본값은 1
Choose = 0 #플레이어 선택, 기본값은 0

#함수 정의
def MAT(): #몬스터 공격 함수 정의, 1턴 소모
    global HP, Turn
    MATK = random.randint(18, 25)
    HP -= MATK
    Turn += 1
    print(f"몬스터가 공격했다! 당신의 남은 HP:{HP}")
    time.sleep(1)
def PAT():
    global MHP
    MHP -= ATK
    print(f"당신은 몬스터를 공격했다! 몬스터의 남은 HP:{MHP}")
def PHEAL():
    global HP
    HP += 40
    print(f"당신은 회복했다! 당신의 남은 HP:{HP}")

#게임 진행
print("당신은 몬스터를 만났다!")
while HP > 0 and MHP > 0:
    print(f"{Turn}번째 턴.")
    Choose = int(input("공격하려면 1을, 회복하려면 2를, 기권하려면 -1을 눌러주세요:" )) #플레이어 공격 휴식 기권 선택
    if(Choose == 1):
        PAT()
    elif(Choose == 2):
        PHEAL()
    elif(Choose == -1):
        break
    else:
        print("잘못된 입력입니다. 턴이 넘어갑니다.")
    time.sleep(1)
    MAT()

#게임 끝, 엔딩
if(Choose == -1): #기권패 루트
    print("기권으로 인해 패배하였습니다.") 
elif(Choose != -1 and HP <= 0): #HP패 루트
    print("HP가 모두 달아 패배하였습니다.")
elif(Choose != -1 and MHP <= 0): #승리 루트
    print("축하합니다! 승리하셨습니다!")
