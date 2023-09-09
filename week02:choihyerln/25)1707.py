import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

t = int(input())    # 테스트케이스

def dfs(start, group):
    global error

    # 만약 사이클이 true라면 재귀탈출한다
    if error:
        return
    
    visited[start] = group    # 해당 그룹으로 등록

    for i in graph[start]:    # start와 연결된 원소 탐색
        if not visited[i]:    # 방문하지 않았다면
            dfs(i, -group)    # 다른 -그룹으로 설정한다.
        elif visited[start] == visited[i]:   # 인접한데 같은 그룹이라면
            error = True      # 이분그래프 아님
            return

for _ in range(t):
    v, e = map(int, input().split())    # 정점 & 간선의 개수
    graph = [[] for _ in range(v+1)]    # 빈 그래프 생성
    visited = [0] * (v+1)               # 방문한 정점 체크
    error = False                       # 이분탐색이 맞는지 체크

    for _ in range(e):
        a,b = map(int, input().split())  # 간선 정보
        graph[a].append(b)               # 그래프에 삽입
        graph[b].append(a)

    for i in range(1, v+1):    # 1부터 정점의 개수
        if not visited[i]:     # 아직 방문하지 않았다면
            dfs(i, 1)          # dfs를 돈다
            if error:          # 만약 에러라면 이분그래프 X
                break          # 탈출
    
    if error:
        print('NO')            # error 뜨면 이분그래프 X
    else:
        print('YES')           # 아니면 yes