
# 1~n번까지 n명의 사람이 원을 이루면서 앉아 있고, 양의 정수 k가 주어진다.

import sys
from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

result = []

# k가 3일 때 계산할 변수
cnt = 1

while len(queue) != 0:
    if cnt % k == 0:
        num = queue.popleft()
        result.append(num)
    else:
        num = queue.popleft()
        queue.append(num)
    cnt += 1

print('<', end='')
for i in range(len(result)-1):
    print('%d, ' %(result[i]), end='')
print(result[-1], end='')
print('>')

