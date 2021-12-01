# 예외 처리 미루기
# 사용하는 곳에서 예외를 처리함
class Animal:
    def cry(self):
        #print("소리를 낸다")
        raise NotImplementedError  # 구현하지 않으면 에러 발생

class Dog(Animal):  #Animal 상속
    #pass
    def cry(self):   # cry 재정의
        print("왈~ 왈~")

class Cat(Animal):
    #pass
    def cry(self):
        print("야~옹 야~옹")

dog = Dog()
dog.cry()

cat = Cat()
cat.cry()

