
global tree
tree = [0] * 1000



def findIndex(node):
    for i in range(len(tree)):
        if tree[i] == node:
            return i
    
    print("node not found")
    return -1



def searchleft(nowindex):
    if tree[nowindex] == '.':
        return
    else:
        print(tree[nowindex],end = '')
        searchleft(nowindex*2)
        searchleft(nowindex*2+1)
    return


def searchmid(nowindex):
    if tree[nowindex] == '.':
        return
    else:
        searchmid(nowindex*2)
        print(tree[nowindex],end = '')
        searchmid(nowindex*2+1)
    return


def searchright(nowindex):
    if tree[nowindex] == '.':
        return
    else:
        searchright(nowindex*2)
        searchright(nowindex*2+1)
        print(tree[nowindex],end = '')
    return
    


def main():
    N = int(input())
    
    for _ in range(N):
        node, left, right = input().split()
        
        if node == 'A':
            tree[1] = node
            tree[2] = left
            tree[3] = right
        
        else:
            now_index = findIndex(node)
            tree[now_index * 2] = left
            tree[now_index * 2 + 1] = right
    
    searchleft(1)
    print()
    searchmid(1)
    print()
    searchright(1)

    
main()