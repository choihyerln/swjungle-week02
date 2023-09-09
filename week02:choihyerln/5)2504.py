import sys
ps = sys.stdin.readline()
stack = []
tmp = 1         # result에 더해주기 전 임시 변수
result = 0      # 결과 변수

for i in range(len(ps)):
    if ps[i] == '(':
        tmp *= 2
        stack.append(ps[i])
    elif ps[i] == '[':
        tmp *= 3
        stack.append(ps[i])

    elif ps[i] == ')':
        if not stack or stack[-1]!='(':
            result = 0
            break
        if ps[i-1]=='(':
            result += tmp
        stack.pop()
        tmp //= 2
    
    elif ps[i] == ']':
        if not stack or stack[-1]!='[':
            result = 0
            break
        if ps[i-1]=='[':
            result += tmp
        stack.pop()
        tmp //= 3
# 결과 출력
if stack:
    print(0)
else:
    print(result)