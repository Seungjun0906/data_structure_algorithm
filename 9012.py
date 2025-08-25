import sys

fast_input = sys.stdin.readline

N = int(fast_input())

open_symbol = "("
close_symbol = ")"

for _ in range(N):
    stack = []
    text = fast_input().strip()
    valid = True

    for symbol in text:
        if symbol == open_symbol:
            stack.append(symbol)
        elif symbol == close_symbol:
            if not stack:
                valid = False
                break
            stack.pop()

    print("YES" if valid and not stack else "NO")


# open이면 스택 추가
# close 면 스택이 비어 있는지 확인
# 비어있다면 NOT VPS return NO
# 비어있지 않다면 스택에서 제거

# (((()())()
# ((
