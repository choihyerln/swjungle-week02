import sys

n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

def bfs(si, sj, ei, ej):
    queue = []
    visited = [[0]*m for _ in range(n)]

    queue.append((si,sj))
    visited[si][sj] = 1

    while queue:
        ci, cj = queue.pop(0)   # 먼저 들어온 거 팝
        # 리턴값
        if (ci, cj) == (ei, ej):
            return visited[ei][ej]
        
        # 이동 조건
        # 4방향, 범위 내, 값이 1, 방문기록 없는거
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and visited[ni][nj]==0:
                queue.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1

print(bfs(0,0,n-1,m-1))