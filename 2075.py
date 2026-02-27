# import sys

# input = sys.stdin.readline

# n = int(input())

# top_n = list(map(int, input().split()))

# top_n.sort()


# for _ in range(n - 1):
#     new_row = list(map(int, input().split()))

#     combined = top_n + new_row

#     combined.sort()

#     top_n = combined[-n:]

# print(top_n[0])


import sys

input = sys.stdin.readline

n = int(input().rstrip())
# N 번쨰 수 오름차순
sequence = [4, 13]
# 4, 13을 이용해서 만들어야함
# +4, +13
# 4 13 44 134 413 444 1313


def solution(n):
    sequence = [4, 13]
    # 4, 13을 이용해서 만들어야함
    # +4, +13
    # 4 13 44 134 413 444 1313

    if n == 1:
        return 4
    if n == 2:
        return 13
