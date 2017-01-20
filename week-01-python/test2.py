## 사람 클래스 - 요소 : 이름, 나이, 성별
## 직장동료 클래서 <- 사람 클래스  + 추가 요소 :직급

class Person:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Collegue(Person):
    rank = "대리"

    # def __init__(self, rank):
    #     self.rank = rank

person1 = Person("장그래", "26", "남자")
person2 = Person("안영이", "30", "여자")
collegue1 = Collegue("김수현", "30", "남자")


print(person1.name)
print(collegue1.rank)


### 고급 : 새로운 사람을 만들때, 입력은 그대로 유지하면서 직
### 직급도 처음 만들어 질 때 입력하도록 변경
