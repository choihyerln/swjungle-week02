import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

deq = deque([i for i in range(1, n+1)])
result = []

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())       # k전까지의 수 pop하고 바로 뒤에 append
    result.append(str(deq.popleft()))   # 3번째 되면 result에 3 추가     
print('<'+', '.join(result)+'>')