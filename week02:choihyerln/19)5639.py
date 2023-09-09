import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:
        return
    mid = end + 1
    
    for i in range(start + 1, end + 1):
        if pre[i] > pre[start]:
            mid = i
            break
    post(start + 1, mid - 1) #왼쪽 트리
    post(mid, end)          #오른쪽 트리
    print(start, mid, end, 'this -> mid')
    print(pre[start])       #루트 노드

post(0, len(pre) - 1)


# # 이진 검색 트릴
# # 노드에 들어있는 키의 값은 106보다 작은 양의 정수
# import sys

# # 노드에 들어있는 키의 값은 106보다 작은 양의 정수
# sys.setrecursionlimit(10 ** 6)

# # 트리의 순회 문제는 항상 함수로 시작과 끝을 받아서
# # 알아낸 루트를 기준으로 왼쪽 서브트리와 
# # 오른쪽 서브트리를 나눠서 재귀호출을 하며 
# # 역전시 return
# # print로 찍어내는 위치만 다르다.

# # 전위 순회이므로 항상 앞에 오는데 문제는 중위 탐색이 주어지지 않아 우측 서브트리의 루트 노드를 알 수 없다는 점이다. 다만 전위 탐색의 특성을 참고하여 처음 만나는 root보다 큰 값을 가진 좌표가 우측 서브 트리의 루트 노드임을 알 수 있다. 그렇다면 더 큰 값을 발견하지 못하는 경우도 있을 것이다.

# # 전위 순
# def postorder(left, right):
#     if left > right:
#         return
#     else:
#         # 분할 기준
#         mid = right + 1
#         print(mid, '!@#$')
#         for i in range(left+1, right+1):
#             # 해당 노드보다 크다면 그 전까지 왼쪽 서브 트리
#             # 해당 원소 이후는 오른쪽 서브 트리
#             if tree[left] < tree[i]:
#                 mid = i
#                 break
#         postorder(left+1, mid-1)
#         postorder(mid, right)
#         print(tree[left])

# tree = []
# while True:
#     try:
#         tree.append(int(sys.stdin.readline()))
#     except:
#         break

# postorder(0, len(tree)-1)