from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 단방향 경로 저장

distance = [-1]*(n+1)   # 탐색 시 -1의 값은 아직 방문하지 않는 노드
distance[x] = 0         # 출발 도시 x에서 x로 가는 최단거리는 항상 0

# bfs 함수
def bfs(start):
    q = deque([x])
    while q:
        now = q.popleft()

        for next in graph[now]:
            if distance[next] == -1:    # 아직 탐색하지 않은 노드라면
                distance[next] = distance[now]+1
                q.append(next)

    # k값이 distance에 있다면 i값 출력, 없다면 -1 출력
    if k in distance:
        for i in range(1, n+1):
            if distance[i] == k:
                print(i)
    else:
        print(-1)
bfs(x)