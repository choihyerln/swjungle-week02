from collections import deque

def bfs():
    # 1. 큐 생성, visited 배열 생성
    q = deque()
    visited =[[[0]*M for _ in range(N)] for _ in range(H)]

    # 2. q에 초기데이터들 삽입, 안익은 토마토 카운트
    cnt = 0
    for h in range(H):      # 전체 순회하며 처리
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:   # 익은 토마토
                    q.append([h,i,j])   # 토마토 위치 저장 (동시 다발적으로 다 퍼지기 때문에)
                    visited[h][i][j] = 1
                elif arr[h][i][j] == 0: # 안익은 토마토 cnt 세기
                    cnt += 1
    
    while q:
        ch,ci,cj = q.popleft()
        
        # 6방향, 범위내, 미방문, arr[]==0
        for dh,di,dj in ((0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(-1,0,0),(1,0,0)):
            nh,ni,nj = ch+dh, ci+di, cj+dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and visited[nh][ni][nj]==0 and arr[nh][ni][nj]==0:
                q.append((nh,ni,nj))
                visited[nh][ni][nj] = visited[ch][ci][cj] + 1
                cnt -= 1    # 안익은 토마토 1개 익음
    
    if cnt==0:
        return visited[ch][ci][cj]-1
    else:
        return -1

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)