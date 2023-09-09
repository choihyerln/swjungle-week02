from collections import deque

n = int(input())    # 보드 크기
k = int(input())    # 사과 개수
# 사과 좌표
apple_list = [tuple(map(int, input().split())) for _ in range(k)]

l = int(input())    # 방향 변환 횟수
# 방향 변환 정보
direction_list = [input().split() for _ in range(l)]

# 시계 방향으로 방향 정의
di,dj = [-1,0,1,0], [0,1,0,-1]
# 방향 전환 테이블
dtable = [0]*10001
for sec,turn in direction_list:
    dtable[int(sec)]=turn
dr = 1  # 오른쪽 방향
snake = deque([(1,1)])     # 좌측상단
time = 0             # 0초

while 1:
    time += 1           # 1초 경과
    ci,cj = snake[0]    # 현재 머리 좌표
    ni,nj = ci+di[dr], cj+dj[dr]    # 진행방향으로 한 칸 이동: (0,1)
    # 벽에 부딪히거나, 뱀 몸에 부딪힌 경우 종료
    if 1<=ni<=n and 1<=nj<=n and (ni,nj) not in snake:
        snake.appendleft((ni,nj))   # 머리위치[0]에 이동좌표 확장
        if (ni,nj) in apple_list:
            apple_list.remove((ni,nj))
        else:               # 사과가 없다면
            snake.pop()     # 꼬리제거
        # 방향 전환
        if dtable[time] == 'D': 
            dr = (dr+1)%4       # 오른쪽 회전
        elif dtable[time] == 'L':
            dr = (dr-1)%4       # 왼쪽 회전
    else:       # 종료
        break  
print(time)    