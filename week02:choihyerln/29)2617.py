import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
# dfs를 통해 나보다 무거운 or 가벼운 구슬이 몇개인지 파악하기 위함
big_lst = [[] for _ in range(n+1)]   # 인덱스보다 큰 수
small_lst = [[] for _ in range(n+1)]    # 인덱스보다 작은 수

for _ in range(m):
    s,e = map(int, input().split())
    big_lst[e].append(s)  # 앞번호의 구슬이 뒷번호의 구슬보다 더 무거움
    small_lst[s].append(e)

visited=[False]*(n+1)
cnts=[0]*(n+1)      # 나보다 큰수, 작은수 개수를 세기 위한 배열

def dfs(init_node, node, graph):
    global visited, cnts
    visited[node] = True

    for next in graph[node]:
        if visited[next]:
            continue

        cnts[init_node] += 1
        dfs(init_node, next, graph)

ans = set()

for i in range(1, n+1):
    # 큰 리스트
    # dfs 결과 과반수를 넘으면 그 값을 set에 넣기
    dfs(i, i, big_lst)
    if cnts[i] >= (n+1)//2:
        ans.add(i)
    # 방문기록 초기화
    # 카운트배열 초기화
    for j in range(1,n+1):
        visited[j] = False
        cnts[j] = 0

    # 작은 리스트
    # dfs 결과 과반수를 넘으면 그 값을 set에 넣기
    dfs(i, i, small_lst)
    if cnts[i] >= (n+1)//2:
        ans.add(i)
    # 방문기록 초기화
    # 카운트배열 초기화
    for j in range(1,n+1):
        visited[j] = False
        cnts[j] = 0

print(len(ans))