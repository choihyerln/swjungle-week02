import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    stack.append(int(input()))

top = stack[-1]
cnt = 1

for i in stack[n-2::-1]:
    if top < i:
        cnt += 1
        top = i
print(cnt)