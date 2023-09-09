import sys
input = sys.stdin.readline
k = int(input())
stack = []

for _ in range(k):
    i = int(input())
    stack.append(i)
    if i == 0:
        stack.pop()
        stack.pop()
        
print(sum(stack))