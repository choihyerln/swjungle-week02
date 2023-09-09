n = int(input())        # 탑의 개수   
tops = list(map(int, input().split()))  # 탑 리스트
stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:    # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)     # 인덱스 + 1 도출
            break
        else:
            stack.pop()
    if not stack:               # 스택이 비어있다면
        answer.append(0)        # 레이저를 수신할 탑이 없다
    stack.append([i, tops[i]])  # 인덱스, 값
print(" ".join(map(str, answer)))

# 동호
# import sys

# input = sys.stdin.readline
# print = sys.stdout.write

# N = int(input())
# arr = list(map(int, input().split()))
# myStack = []
# ans = arr

# for i in range(N, 0, -1):
#     if myStack:
#         while myStack:
#             if arr[i - 1] >= arr[myStack[-1]]:
#                 ans[myStack[-1]] = i
#                 # print(str(i) + ' ')
#                 myStack.pop()
#             else:
#                 break
#     myStack.append(i - 1)

# while myStack:
#     ans[myStack[-1]] = 0
#     # print(str(0) + ' ')
#     myStack.pop()

# for i in ans:
#     print(str(i) + " ")