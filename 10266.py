import sys

fast_input = sys.stdin.readline

# 바늘의 수
N = int(fast_input())

# 원소들이 모두 다름

clock_1 = list(map(int, fast_input().split()))

clock_2 = list(map(int, fast_input().split()))


# 이미 동일한 배열의 원소와 인덱스 값이라면 possible
if clock_1 == clock_2:
    print("possible")

candidate = clock_1.copy()
# 하나를 고정하고 하나만 회전 시킨다.
for _ in range(N):
    last_num = candidate[-1:]
    arr = candidate[0 : N - 1]

    candidate = last_num + arr

    print("candidate", candidate)
    print("clock2", clock_2)
    if candidate == clock_2:
        print("possible")

print("impossible")
