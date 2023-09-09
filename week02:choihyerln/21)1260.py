from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 양방향 처리해줌
# graph[a] = a에서 갈 수 있는 노드들의 집합
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:            # 큐 리스트가 빌 때까지 반복
        p = queue.popleft()
        print(p, end=" ")
        for i in graph[p]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# dfs
visited = [False] * (n+1)
dfs(v)
print()

# bfs
visited = [False] * (n+1)
bfs(v)