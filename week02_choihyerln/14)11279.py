import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
max_heap = []

for _ in range(n):
    x = int(input())
    if x > 0 :
        hq.heappush(max_heap, (-x,x))
    elif x == 0:
        if max_heap:
            print(hq.heappop(max_heap)[1])
        else:
            print(0)