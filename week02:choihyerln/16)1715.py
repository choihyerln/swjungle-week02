import sys
import heapq as hq

n = int(sys.stdin.readline())
cards = []

for _ in range(n):
    hq.heappush(cards, int(sys.stdin.readline()))
result = 0

if len(cards) == 1:
    print(result)

else:
    for i in range(n-1):    # 2개씩 꺼내기 때문에 n-1
        pre = hq.heappop(cards)     # 가장 작은 수
        cur = hq.heappop(cards)     # 그 다음 작은 수

        result += pre + cur
        hq.heappush(cards, pre + cur)
    
    print(result)