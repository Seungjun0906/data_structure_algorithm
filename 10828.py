import sys

fast_input = sys.stdin.readline

N = int(fast_input())


class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) >= 1:
            print(self.stack.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.stack))

    def empty(self):
        print(int(len(self.stack) == 0))

    def top(self):
        if len(self.stack) == 0:
            print(-1)
        else:
            print(self.stack[len(self.stack) - 1])

    def operation(self, type: str, val=""):

        if type == "push":
            return getattr(self, type)(val)

        return getattr(self, type)()


stack = Stack()

for _ in range(N):

    inputs = list(fast_input().split())

    method = inputs[0]

    num = 0

    if len(inputs) > 1:
        method = inputs[0]
        num = int(inputs[1])

    if method == "push":
        stack.operation("push", num)
        continue

    stack.operation(method)
