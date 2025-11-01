import sys

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()


def build_pi(p: str):
    m = len(p)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(s: str, p: str) -> int:
    n, m = len(s), len(p)
    if m == 0:
        return 1  # 빈 패턴은 항상 부분문자열
    pi = build_pi(p)
    j = 0
    for i in range(n):
        while j and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            j += 1
            if j == m:
                return 1
    return 0


print(kmp(s, p))
