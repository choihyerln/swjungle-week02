import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    stack = []
    ps = input()

    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()     # '('와 ')' 개수 맞으면 stack 비워짐 
            else:
                print("NO")     # 비어있는 상태에서 ')' 들어가면 무조건 NO
                break
            
    else:   # break문으로 끊기지 않고 수행 됐을 경우
        if not stack:               # 스택 비어있으면
            print("YES")            # YES
        else:
            print("NO")