




def dfs(arr):
    if len(arr) == M:
        for k in range(len(arr)):
            print(arr[k], end = ' ')
        print()
        return
    
    
    for i in range(1, N + 1):
        if len(arr) == 0:
            arr.append(i)
            dfs(arr)
            arr.pop()
        
        elif arr[-1] <= i:
            arr.append(i)
            dfs(arr)
            arr.pop()
    
    return

def main():
    global N,M
    N,M = map(int,input().split())
    
    dfs([])
    
    
    
main()