import heapq as hq
import sys
input = sys.stdin.readline

N = int(input())
h_o = []
for _ in range(N):
    x = list(map(int, input().strip().split()))
    h_o.append(sorted(x))
train = int(sys.stdin.readline().strip())
h_o = [*filter(lambda x: x[1] - x[0] <= train, h_o)]
h_o.sort(key=lambda x: x[1])    # 큰 점 기준으로 오른차순 정렬

possible = []
ans = 0

for ho in h_o:
    if not possible:
        hq.heappush(possible, ho)
    else:
        while possible[0][0] < ho[1] - train:   # 힙에 존재하는 가장 작은 점이 철로의 끝점 안에 있는지
            hq.heappop(possible)
            if not possible:
                break
        hq.heappush(possible, ho)
    ans = max(len(possible), ans)
print(ans)