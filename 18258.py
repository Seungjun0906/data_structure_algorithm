from collections import deque
from sys import stdin


dq = deque()

N = int(stdin.readline())

for _ in range(N):
    arr = stdin.readline().split()
    
    method = arr[0]

    if method == 'push':
        dq.append(arr[1])
    if method == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    if method == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    if method == 'size':
        print(len(dq))
    if method == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if method == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())