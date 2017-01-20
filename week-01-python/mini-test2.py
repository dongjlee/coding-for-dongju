## 클래스 복습
## 학교 클래스 만들기
## 이름, 설립연도, 주소 in class
## 클래스를 활성화 할 때, 위의 3가지 데이터를
## 반드시 입력하도록 처리해봅시다.

class School:

    def __init__(self, name, date, adress):
        self.name = name
        self.date = date
        self.adress = adress

school1 = School("대연고", "1980", "부산시 남구 대연동")
print(school1.name)
