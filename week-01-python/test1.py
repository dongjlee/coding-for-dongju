## 처음 실행 시 "한식, 중식, 일식 중 한 가지를 고르세요"
## 그 중에서 한 가지를 고르면 식당 이름을 하나로 임의로 추천해줍니다.

## 힌트 : 리스트를 여러개 사용하고 사용자의 입력을 받아야 합니다.

korea = ["김치찌개집", "설렁탕집", "감자탕집"]
china = ["복성각", "일품향", "짬뽕잘하는집"]
japan = ["미츠루", "간사이소바", "갓덴스시"]
menu = input("한식, 중식, 일식 중 한 가지를 고르세요")
if menu == "한식":
    import random
    print(random.choice(korea))
elif menu == "중식":
    import random
    print(random.choice(china))
else:
    import random
    print(random.choice(japan))
