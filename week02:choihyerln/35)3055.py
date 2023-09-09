import sys
from collections import deque

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
dx, dy = [-1,1,0,0],[0,0,-1,1]

q = deque()

def bfs(dx,dy):
    while q:
        x,y = q.popleft()
        # 입력 받은 값이 출발 지점이라면, 즉 S가 D에 도착했을 경우
        if graph[dx][dy] == 'S':
            return visited[dx][dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (graph[nx][ny] != '*') and graph[x][y] == 'S':
                    graph[nx][ny] == 'S'
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                elif (graph[nx][ny] != 'D') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx,ny))
    return "KAKTUS"

for x in range(r):
    for y in range(c):
        if graph[x][y] == 'S':
            q.append((x,y))
        elif graph[x][y] == 'D':
            dx,dy = x,y

for x in range(r):
    for y in range(c):
        if graph[x][y] == '*':
            q.append((x,y))

print(bfs(dx,dy))