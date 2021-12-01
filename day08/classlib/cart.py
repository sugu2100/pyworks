# Cart 클래스 만들기 - 장바구니

class Cart:
    li = [] # 빈 리스트 생성(클래스 리스트)

    def __init__(self, goods):
        Cart.li.append(goods)  #Cart이름으로 접근

    def __str__(self):
        return Cart.li

cart1 = Cart("계란")
#print(cart1.li)

cart2 = Cart("두부")
#print(cart2.li)

cart3 = Cart("커피")
print(cart3.li)
