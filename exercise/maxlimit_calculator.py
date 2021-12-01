from exercise.calculator import Calculator
# value가 100 이상의 값은 가질 수 없도록 제한하기
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

        return self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)