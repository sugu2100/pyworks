# GoldCustomer 클래스 정의 - Customer를 상속받음
from day09.class_lib.customer import Customer

class GoldCustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid, name)  #부모 멤버 상속
        self.cgrade = "GOLD"         #골드 등급
        self.sale_ratio = 0.1        #구매 할인율 10%
        self.bonus_ratio = 0.02      #보너스 적립율 2%

    def calc_price(self, price): #부모 메서드 재정의
        price -= int(price * self.sale_ratio)
        #할인된 가격 = 가격 - (가격 x 구매 할인율)
        self.bonus_point += int(price * self.bonus_ratio)
        return price
