## 사용자에게 가위, 바위, 보를 물어봅니다.
## 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고, 승패를 가릅니다.
## 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.

## hint : 한개의 리스트 사용, 사용자의 입력을 받아야.
## hint : 램덤 뽑기 다시 사용
## hint : 컴퓨터에게 승, 패를 가르쳐줘야 합니다.

weapon = ["가위", "바위", "보"]
win = 0
lose = 0

while(win < 3 or lose < 3):
    user = input("가위~ 바위~ 보!?")
    import random
    com = random.choice(weapon)
    play = (user, com)

    if user == com:
        print("당신=", user, "컴퓨터=", com, "/ 결과 : 비김")
    elif play == ("가위", "바위"):
        lose = lose + 1
        print("당신=", user, "컴퓨터=", com, "/ 결과 : 패")
    elif play == ("바위", "보"):
        lose = lose + 1
        print("당신=", user, "컴퓨터=", com, "/ 결과 : 패")
    elif play == ("보", "가위"):
        lose = lose + 1
        print("당신=", user, "컴퓨터=", com, "/ 결과 : 패")
    else:
        win = win + 1
        print("당신 =", user,"/", "컴퓨터 =", com, "/ 결과 : 승")
    if win == 3:
        break
    elif lose == 3:
        break

if win == 3:
    print("You win", "결과", win, "승", lose, "패")
elif lose == 3:
    print("You lose", "결과", win, "승", lose, "패")
