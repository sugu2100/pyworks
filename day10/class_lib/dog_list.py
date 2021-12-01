# Dog 클래스 만들기
class Dog:
    #tricks = []   #클래스 리스트

    def __init__(self, name):
        self.name = name
        self.tricks = []  #인스턴스 멤버 리스트

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog("Elsa")
dog2 = Dog("Buddy")

dog1.add_trick("play dead")
dog2.add_trick("roll over")

print(dog1.tricks)
print(dog2.tricks)