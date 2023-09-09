# 다익스트라 알고리즘
from sys import maxsize
import sys
import heapq as hq

input = sys.stdin.readline
# 도시 개수, 버스 개수
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
total_cost = [maxsize]*(n+1)

for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((b, cost))  # 출발하는 경로에 도착 도시와 소요 비용을 튜플로 묶어 넣어줌

# 출발 도시 번호, 도착 도시 번호
start, end = map(int, input().split())

# 다익스트라 구현
def dijkstra(start):
    total_cost[start] = 0   # 시작점 비용 0
    heap = []
    hq.heappush(heap, [0, start])   # heap push를 통해 비용과 현재 좌표 리스트로 넣어줌

    while heap:
        cost, now = hq.heappop(heap)
        if total_cost[now] < cost:
            continue
            # 지금 비용이 heap에 담긴 비용보다 작으면 넘어감
        for t, v in graph[now]:
            new_cost = cost + v  # 여태까지 들었던 비용에 경로의 비용을 더해
            if total_cost[t] > new_cost:
                total_cost[t] = new_cost
                hq.heappush(heap, [new_cost, t])

dijkstra(start)
print(total_cost[end])