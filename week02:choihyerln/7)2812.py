n, k = map(int, input().split())
nums = list(input())
stack = []
count = 0
for i in range(n):
    while k > count and stack and stack[-1] < nums[i]:
        stack.pop()
        count += 1
    stack.append(nums[i])

print(''.join(stack[:n-k]))