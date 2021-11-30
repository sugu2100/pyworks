# Converter 클래스 정의
# 온도 변환기 : 화씨온도(F) = 섭씨온도(C) x 1.8 + 32
from day09.class_lib.scaleconverter import ScaleConverter

class Converter(ScaleConverter):  # ScaleConverter 상속 받음
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor) #'C', 'F', 1.8
        self.offset = offset    #32

    def convert(self, value): # 부모 메서드 재정의(overriding)
        return self.factor * value + self.offset #(단위1 값 x 수) + 단위2 값

conv = Converter('C', 'F', 1.8, 32)
print("Converting 21C")
#print(str(conv.convert(21)) + conv.units_to)
print("%.2fF" % conv.convert(21))
