import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 방향 없는 그래프
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 기록 리스트 초기화
visited = [False] * (n+1)
cnt = 0

# dfs 구현
def dfs(start):
    visited[start] = True
    # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행(재귀)
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

for i in range(1, n+1):
    # 방문하지 않았던 노드만 탐색하고 cnt 횟수 +1
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)