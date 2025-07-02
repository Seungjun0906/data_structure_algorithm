# 윤년 Y = 1 N = 0
# 4의 배수 &&  not 100 배수 i.g) 2012
# 400의 배수  i.g) 2000
import sys

fast_input = sys.stdin.readline

Y = int(fast_input())

remainder_4 = Y % 4 == 0
remainder_100 = Y % 100 == 0
remainder_400 = Y % 400 == 0

if remainder_4 and not remainder_100:
    print(1)
elif remainder_400:
    print(1)
else:
    print(0)
