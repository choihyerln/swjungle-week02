from collections import deque

N, M = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]

ice = []
for i in range(N):
    for j in range(M):
        if ocean[i][j]:
            ice.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not ocean[nx][ny]:
                    sea += 1
                elif ocean[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        ocean[x][y] = max(0, ocean[x][y]-sea)
    
    return 1

while ice:
    visited = [[False] * M for _ in range(N)]
    delList = []
    group = 0

    for i, j in ice:
        if not visited[i][j] and ocean[i][j]:
            group += bfs(i, j)
        if ocean[i][j] == 0:
            delList.append((i,j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)