
from math import inf
from sys import stdin


MAX = 100000

min_tree = [0 for i in range(MAX * 4)]
max_tree = [0 for i in range(MAX * 4)]
arr = []

def tree(node, start, end):    
    global min_tree, max_tree
    
    if start == end:
        min_tree[node] = arr[start]
        max_tree[node] = arr[start]
        return

    mid = (start + end) // 2
    tree(node * 2, start, mid)
    tree(node * 2 + 1, mid + 1, end)
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1])
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1])
    return


def minquery(node, start, end, left, right):
    if left > end or right < start:
        return inf
    
    if left <= start and right >= end:
        return min_tree[node]
    
    mid = (start + end) // 2
    return min(minquery(node * 2, start, mid, left, right), minquery(node * 2 + 1, mid + 1, end, left, right))


def maxquery(node, start, end, left, right):
    if left > end or right < start:
        return -inf
    
    if left <= start and right >= end:
        return max_tree[node]
    
    mid = (start + end) // 2
    return max(maxquery(node * 2, start, mid, left, right), maxquery(node * 2 + 1, mid + 1, end, left, right))
    
    

def main():
    N,M = map(int,input().split())
    
    for _ in range(N):
        arr.append(int(stdin.readline()))
        
    tree(1, 0, N-1)
    
    
    for _ in range(M):
        a,b = map(int,stdin.readline().split())
        print(minquery(1, 0, N-1, a-1, b-1), maxquery(1, 0, N-1, a-1, b-1))
    
    
    
    
main()