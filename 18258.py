from collections import deque
from sys import stdin


dq = deque()

N = int(stdin.readline())

for _ in range(N):
    arr = stdin.readline().split()

    method = arr[0]

    if method == "push":
        dq.append(arr[1])
    if method == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    if method == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    if method == "size":
        print(len(dq))
    if method == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if method == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())


#             백준 18258 큐 2: 직접 구현 vs deque, 그리고 선택 이유
# 이 글에서는 큐를 직접 구현한 버전과 collections.deque를 활용한 버전을 나란히 소개하고, 왜 실전에서는 deque를 쓰는지 핵심 이유를 정리합니다.
# 직접 큐 구현 (리스트 + head 인덱스, O(1) pop)
# 리스트의 앞에서 요소를 꺼내면 O(n)이므로, 앞에서 실제로 삭제하지 않고 head 포인터만 증가시키는 방식으로 O(1) pop을 달성합니다.
# Apply to 1157.py
# )
# 시간복잡도: push, pop, front, back, empty, size 모두 O(1)
# 주의: head가 커지며 리스트 앞부분이 “논리적으로만” 비워짐(메모리 회수 없음). 문제 크기 내에서는 안전.
# deque 버전 (간결하고 안전한 표준 해법)
# )
# append, popleft가 모두 O(1) 보장.
# 코드가 간결하고, 인덱스 관리가 필요 없어 실수 여지가 적음.
# 왜 deque를 쓰는가?
# O(1) 양끝 연산 보장: append, appendleft, pop, popleft 모두 평균 O(1). 리스트의 pop(0)은 O(n)이라 대량 연산에서 시간초과 위험.
# 구현 안정성: 인덱스 포인터 관리 없이도 올바른 동작. 실수 가능성·디버깅 비용이 낮음.
# C로 최적화: CPython에서 deque는 C로 만들어져 실제 런타임이 빠르고 일관적.
# 가독성: 의도가 명확해 코드 리뷰·협업에 유리.
# 직접 구현(head 인덱스) 방식도 충분히 빠르지만, 실전(특히 백준 대용량 입출력)에서는 deque가 더 간단하고 안전한 “표준 해법”입니다. 단, 최적 입출력을 위해 sys.stdin.readline과 출력 버퍼링(예: '\n'.join(...))을 함께 쓰면 추가로 시간을 절약할 수 있습니다.
# 복잡도 한눈에 비교
# 직접 구현(head 인덱스): 모든 연산 O(1), 메모리 회수는 안 됨(문제 스케일 내 무관).
# deque: 모든 연산 O(1), 구현 간결/안전, 실전에서 권장.
# 간단 요약
# 직접 구현: 리스트 + head 인덱스 증가로 O(1) pop 확보.
# deque: 더 간결하고 실수 적으며 C 최적화로 빠름.
# 입출력 최적화: sys.stdin.readline, 출력 모아서 한 번에 쓰기 추천.
