import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(root):
    for i in graph[root]:
        if visited[i] == 0:
            visited[i] = root    # 각 노드의 부모노드를 찾아라
            dfs(i)
dfs(1)

for x in range(2, n+1):
    print(visited[x])