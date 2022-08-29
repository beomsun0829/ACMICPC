N = 0
visited = [False] * 100


def dfs(now, arr):
    if(visited[now]):
        return

    visited[now] = True
    dfs(arr[now], arr)

    return

def dfsall(arr):
    global N
    cnt = 0
    
    for i in range(0, N):
        if(visited[i] == False):
            dfs(i, arr)
            cnt += 1
    
    return cnt


def main():
    global N
    N = int(input())
    arr = input().split()

    for i in range(N):
        arr[i] = int(arr[i])
    
    
    cnt = dfsall(arr)
    
    if cnt == 1:
        print(0)
    else:
        print(cnt)
    


main()