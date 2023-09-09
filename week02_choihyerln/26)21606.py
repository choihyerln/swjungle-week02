import sys
sys.setrecursionlimit(10**9)
# 정점의 수
n = int(sys.stdin.readline())
ans = 0   # 산책 경로 카운트
# location 정보 받아오기
location = [0]+list(map(int, sys.stdin.readline().strip()))
# 1번 노드부터 n번까지 받아오기 위해 빈 공간 생성
graph = [[] for _ in range(n+1)]
# 방문목록
visited = [0] * (n+1)

def dfs(v, cnt):
    visited[v] = True
    for i in graph[v]:  # 노드 v와 인접한 노드 하나씩 불러옴
        if location[i] == 1:    # 그 중 실내이면
            cnt += 1
        elif location[i] == 0 and not visited[ i]:
            cnt = dfs(i, cnt)   # 해당 실외점을 기준으로 dfs를 돈다
    return cnt

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    # 실내 - 실내 바로 연결된 경우
    if location[a] == 1 and location[b] == 1:   # 둘 다 실내이면
        ans += 2

hap = 0

for i in range(1, n+1):
    if not visited[i] and location[i] == 0: # 방문하지 않은 노드 중 실외라면
        x = dfs(i, 0)
        hap += x*(x-1)
print(hap)