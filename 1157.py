import sys
from collections import Counter

s = sys.stdin.readline().strip().upper()
cnt = Counter(s)
top2 = cnt.most_common(2)
print("?" if len(top2) > 1 and top2[0][1] == top2[1][1] else top2[0][0])
