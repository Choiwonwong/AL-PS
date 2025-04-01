# 트리 순회
# https://www.acmicpc.net/problem/1991
# 이진 트리라서 graph보단 리스트로 접근할지 고민 중 -> 근데 다만 완전이진트리가 아니라서, 리스트 길이 제한이 어려움.
# 그냥 그래프로 가고 전위탐색부터 진행하기

# from collections import defaultdict, deque
# import sys

# N = int(input())
# parent_graph = defaultdict(list)
# child_graph = defaultdict(list)
# for _ in range(N):
#     parent, left_child, right_child = sys.stdin.readline().rstrip().split()
#     if left_child != ".":
#         parent_graph[parent].append(left_child)
#         child_graph[left_child].append(parent)
#     if right_child != ".":
#         parent_graph[parent].append(right_child)
#         child_graph[right_child].append(parent)

# print(parent_graph)
# print(child_graph)

# stack_for_first = ['A']
# visited_for_first = set()
# result_for_first = []
# leaf_start = None
# while stack_for_first:
#     node = stack_for_first.pop()
#     result_for_first.append(node)
#     visited_for_first.add(node)
#     if test is None and len(graph[node]) == 0:
#         leaf_start = node
#     for neighbor in reversed(graph[node]):
#         if neighbor in visited_for_first:
#             continue
#         stack_for_first.append(neighbor)


# 중위 순회 하려면 왼 -> 루 -> 오
# 후위 순회 하려면 왼 -> 오 -> 루 

# 근데 이진트리라서 그래프로 접근하기 힘든 듯
# 근데 N 26개면?
## 조금 있다가 다시 보기

import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 트리 구성
N = int(input())  # 첫 줄: 노드 개수
tree = {}

for _ in range(N):
    parent, left, right = sys.stdin.readline().rstrip().split()

    # 부모 노드가 없으면 생성
    if parent not in tree:
        tree[parent] = Node(parent)

    # 왼쪽 자식
    if left != ".":
        tree[left] = tree.get(left, Node(left))
        tree[parent].left = tree[left]

    # 오른쪽 자식
    if right != ".":
        tree[right] = tree.get(right, Node(right))
        tree[parent].right = tree[right]

# 루트 노드 찾기 (입력에서 첫 번째로 등장한 노드가 루트)
root = tree["A"]  # 문제에서 항상 A가 루트라고 가정

# 전위 순회 (Preorder: Root → Left → Right)
def preorder(node):
    if node:
        print(node.value, end="")
        preorder(node.left)
        preorder(node.right)

# 중위 순회 (Inorder: Left → Root → Right)
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end="")
        inorder(node.right)

# 후위 순회 (Postorder: Left → Right → Root)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end="")

preorder(root)
print()
inorder(root)
print()
postorder(root)