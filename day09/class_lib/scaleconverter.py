# ScaleConverter 클래스 정의
# inch를 mm로 변환하기 : 1inch -> 25mm
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from    # 단위 1 (inches)
        self.units_to = units_to        # 변환할 단위(mm)
        self.factor = factor            # 변환 요소(값) - 25

    def convert(self, value): #변환 계산 함수
        return self.factor * value  # 변환 값 x 숫자

if __name__=="__main__":
    sc = ScaleConverter("inches", "mm", 25)
    print("Converting 2 inches")
    print(str(sc.convert(2)) + sc.units_to)