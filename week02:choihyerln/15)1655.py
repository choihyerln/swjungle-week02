import sys
import heapq as hq

n = int(sys.stdin.readline())

leftheap = []
rightheap = []

for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftheap) == len(rightheap):
        hq.heappush(leftheap, -num)     # 최대힙
    else:   # 개수가 left가 하나 더 많을 때
        hq.heappush(rightheap, num)     # 최소힙
    
    if rightheap and rightheap[0] < -leftheap[0]:
        leftVal = hq.heappop(leftheap)
        rightVal = hq.heappop(rightheap)

        hq.heappush(leftheap, -rightVal)
        hq.heappush(rightheap, -leftVal)

    print(-leftheap[0])