import decimal
import os

precision = int(input('请输入需要计算的圆周率位数：'))
decimal.getcontext().prec = precision + 1

def compute_pi():
    pi = decimal.Decimal(0)
    k = 0
    while True:
        pi += decimal.Decimal(1) / (16 ** k) * (
            decimal.Decimal(4) / (8 * k + 1) -
            decimal.Decimal(2) / (8 * k + 4) -
            decimal.Decimal(1) / (8 * k + 5) -
            decimal.Decimal(1) / (8 * k + 6))
        k += 1
        yield pi

pi_generator = compute_pi()
a = next(pi_generator)
sss = 0
while True:
    sss += 1
    if sss % 100 == 0:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('正在计算……,临时值：'+str(a))
    b = a
    a = next(pi_generator)
    if a == b:
        os.system('clear' if os.name == 'posix' else 'cls')
        print('结果是:'+str(next(pi_generator)))
        break
