# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
from decimal import Decimal

def rounding(num, roond):
    return num.quantize(Decimal(roond))


num1 = Decimal(input("Enter a real number: "))
num2 = Decimal(input("Enter the required accuracy '0.0001': "))

print(rounding(num1, num2))