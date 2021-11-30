# VIPCustomer 클래스 정의
from day09.class_lib.customer import Customer

class VIPCustomer(Customer):

    def __init__(self, cid, name, agent):
        super().__init__(cid, name)   #부모 멤버 상속
        self.agent = agent            #전문 상담원 멤버
        self.cgrade = "VIP"           #VIP 등급
        self.sale_ratio = 0.1         #구매할인율 10%
        self.bonus_ratio = 0.05       #보너스 적립율 5%

    def calc_price(self, price):  # 부모 메서드 재정의
        price -= int(price * self.sale_ratio)
        # 할인된 가격 = 가격 - (가격 x 구매 할인율)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):  # 부모 정보 상속
        return super().__str__() + "\n전문 상담원 ID는 {}입니다.".format(self.agent)

