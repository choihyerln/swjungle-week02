from collections import deque

n = int(input())    # 완제품 번호
m = int(input())  
graph = [[] for _ in range(n+1)]        # 연결 정보
inDegree = [0 for _ in range(n+1)]      # 진입 차수
needs = [[0]*(n+1) for _ in range(n+1)] # 각 제품을 만들 때 필요한 부품 2차원 배열

q = deque()     # 위상정렬
for _ in range(m):
    x,y,k = map(int, input().split())   # x = y를 k개 조립해서 만듦
    graph[y].append((x,k))
    inDegree[x] += 1

for i in range(1, n+1):
    if inDegree[i] == 0:      # 진입차수가 0이라면
        q.append(i)           # q에 넣어준다

# 위상정렬 시작
while q:
    now = q.popleft()
    for next, next_need in graph[now]:
        # 현 제품이 기본 부품이면
        if needs[now].count(0) == n+1:
            needs[next][now] += next_need
        # 현 제품이 중간 부품이면
        else:
            for i in range(1, n+1):
                needs[next][i] += needs[now][i] * next_need
        # 진입차수 -1
        inDegree[next] -= 1
        if inDegree[next] == 0:     # 진입차수 0되면
            q.append(next)          # q에 넣어라

for x in enumerate(needs[n]):
    if x[1] > 0:
        print(*x)