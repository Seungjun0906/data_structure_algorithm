import sys 

# def comparison(a,b):
#     if num1 > num2:
#         print(">")
#     elif num1 < num2:
#         print("<")
#     else:
#         print("==")
    

# num1,num2 = list(map(int,sys.stdin.readline().split()))

# comparison(num1,num2)    

# def test_score(score):
#     if 90 <= score <= 100:
#         print("A")
#     elif 80 <= score <= 89:
#         print("B")
#     elif 70 <= score <= 79:
#         print("C")
#     elif 60 <= score <= 69:
#         print("D")
#     else:
#         print("F")
        
# num = int(sys.stdin.readline())

# test_score(num)

# def is_leap_year(year):
#     # 4의 배수
#     # not 100의 배수 or 400의 배수
#     if year % 4 == 0:
#         if year % 100 != 0 or year % 400 == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         print(0)
        
# num = int(sys.stdin.readline())

# is_leap_year(num)

def quadrant(x,y):
    #+ + quadrant1
    if x > 0 and y > 0:
        print(1)
    #- + quadrant2
    elif x < 0 and y > 0:
        print(2)
    #- - quadrant3
    elif x < 0  and  y < 0:
        print(3)
    else:
    #+ - quadrant4
        print(4)
    


num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

quadrant(num1,num2)
