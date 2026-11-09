import random
from time import sleep

dealerhp=5
userhp=5
round=0
userinven=[] #8이 최대
dealerinven=[] #8이 최대
ammo=0
blank=0
clip=[]
clipnum=0
itemget=''
itemgetlist=[]
username=''
useract=''
target=''
whichitem=''
turn='user'
itemrule=''
know=0 #0은 아는거/1은 모르는거

#아이템 목록
#구급상자/강탈 | 돋보기/비열 | 인버터/변화 | 톱날/증오 | 언로더/증발 | 수갑/억제 | 대포폰/정보통신

print('inspired by buckshot roulette')
print('version-1.0')
sleep(2)
if input('게임을 시작하시겠습니까?(y/n)') != 'y':
    quit

def shoot():
    global clip,dealerhp,userhp,target
    for i in range(3):
        print('.')
        sleep(1.5)
    if clip[0]=='ammo' or clip[0]=='ammo2':
        print('!')
        if target == 'dealer':
            print('딜러에게 효과가 굉장했다!')
            if clip[0]=='ammo':
                dealerhp -= 1
            elif clip[0]=='ammo2':
                dealerhp -=2
        elif target == 'user':
            print('당신은 의식이 흐려져 가는 것을 느꼈다.')
            if clip[0]=='ammo':
                userhp -= 1
            elif clip[0]=='ammo2':
                userhp -= 2
        if turn == 'user':
            turn='dealer'
        elif turn == 'user2':
            turn='user'
    elif clip[0]=='blank':
        print('.')
        if target == 'dealer':
            print('아무 일도 일어나지 않았다.')
            if turn == 'user':
                turn='dealer'
            elif turn == 'user2':
                turn == 'user'
        elif target == 'user':
            print('아무 일도 일어나지 않았다.')
    clip.pop(0)
    clipnum -= 1

print('면책 동의서를 작성해.')
print('''-면책 동의서
본인은 이 게임의 위험성을 알고 있으며 강요 받지 않고 자발적으로 참여했습니다.''')
sleep(2)
username=input('당신의 이름을 적어 서명하세요:')
itemrule=input('아이템에 대한 설명을 들을건가?(Y/N)')
if itemrule=='Y' or itemrule=='y':
    print('''\
        아이템은 버키를 재장전 할 때 마다 4개 씩 보급된다.
        다음은 각 아이템에 대한 설명이다.
        구급상자:전기 충격기를 1개 얻는다. 5개 이상 얻을 수 없다.
        돋보기:다음 탄환의 종류를 확인한다.
        인버터:다음 탄환의 극성을 변경한다.
        톱날:다음 탄환이 실탄이라면 2배의 피해를 입힌다.(상대는 전기 충격기 2개를 사용해야 생존할 수 있다.)
        언로더:다음 탄환을 제거한다.
        수갑:상대는 다음 턴을 건너 뛴다.
        대포폰:현재 기준으로 3번째 탄환의 종류를 확인한다.
        ''')

while not round==3:
    round+=1
    print('{}라운드.'.format(round))
    while dealerhp>=1 and userhp>=1:
        clipnum=random.choice([5,6,7,8])
        if clipnum==5:
            ammo=random.choice([2,3])
        elif clipnum==6:
            ammo=random.choice([2,3,4])
        elif clipnum==7:
            ammo=random.choice([3,4])
        elif clipnum==8:
            ammo=random.choice([3,4,5])
        blank=clipnum-ammo
        for i in range(ammo):
            clip.append('ammo')
        for i in range(blank):
            clip.append('blank')
        random.shuffle(clip)
        print('실탄: {}/공포탄: {}'.format(ammo,blank))
        sleep(2)
        for i in range(4):
            if not len(userinven)==8:
                itemget=random.choice(['구급상자','돋보기','언로더','인버터','톱날','수갑'])
                itemgetlist.append(itemget)
                userinven.append(itemget)
            if not len(dealerinven)==8:
                dealerinven.append(random.choice(['구급상자','돋보기','언로더','인버터','톱날','수갑']))
        print('당신은',itemgetlist,'을 얻었습니다.')
        itemgetlist=[]
        turn='user'
        while not clipnum==0:
            print('딜러의 전기 충격기:{} / '.format(dealerhp),username,'의 전기 충격기:{}'.format(userhp))
            sleep(1)
            if turn == 'user' or turn == 'user2':
                useract=input('버키 / 인벤토리')
                if useract=='버키':
                    target=input('대상을 정하세요(딜러/나)')
                    if target != '딜러' and target !='나':
                        continue
                    shoot()
                elif useract=='인벤토리':
                    print(userinven)
                    whichitem=input('사용할 아이템을 입력해 주세요')
                    if whichitem in userinven:
                        if whichitem=='구급상자':
                            if userhp<5:
                                userhp+=1
                            print('당신은 전기 충격기를 1개 얻었다.')
                        elif whichitem=='돋보기':
                            if clip[0]=='ammo':
                                print('당신은 1번째 탄환이 실탄임을 확인했다.')
                            else:
                                print('당신은 1번째 탄환이 공포탄임을 확인했다.')
                        elif whichitem=='인버터':
                            if clip[0]=='ammo':
                                clip[0]='blank'
                            else:
                                clip[0]='ammo'
                            print('극성을 변경했다.')
                        elif whichitem=='톱날':
                            if clip[0]=='ammo':
                                clip[0]='ammo2'
                            print('당신은 톱날을 사용했다.')
                        elif whichitem=='언로더':
                            clip.pop(0)
                        elif whichitem=='수갑':
                            turn='user2'
                        elif whichitem== '대포폰':
                            try:
                                if clip[2]=='ammo':
                                    print('당신은 3번째 탄환이 실탄이라는 것을 확인했다.')
                                elif clip[2]=='blank':
                                    print('당신은 3번째 탄환이 공포탄이라는 것을 확인했다.')
                            except IndexError:
                                print('딜러가 당신을 한심한 눈빛으로 본다.')
                else:
                    print('정확히 입력해라.')
                    continue
            elif turn == 'dealer' or turn == 'dealer2':
                if dealerhp<5 and '구급상자' in dealerinven:
                    dealerhp+=1
                    dealerinven.remove('구급상자')
                    print('딜러는 구급상자를 사용했다.')
                if '돋보기' in dealerinven:
                    pass