n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

maxi = int(-1e9)
mini = int(1e9)

def dfs(depth, total, plus, minus, multi, divide):
    global maxi, mini

    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if plus:
        dfs(depth+1, total+a[depth], plus-1, minus, multi, divide)
    
    if minus:
        dfs(depth+1, total-a[depth], plus, minus-1, multi, divide)
    
    if multi:
        dfs(depth+1, total*a[depth], plus, minus, multi-1, divide)
    
    if divide:
        dfs(depth+1, int(total/a[depth]), plus, minus, multi, divide-1)

dfs(1, a[0], op[0], op[1], op[2], op[3])
print(maxi)
print(mini)