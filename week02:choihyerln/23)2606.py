n = int(input())    # 컴퓨터의 수
m = int(input())    # 직접 연결되어 있는 컴퓨터 쌍의 수
graph = [[] for _ in range(n+1)]

# 무방향 그래프
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
cnt = 0

def dfs(start):
    global cnt
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)