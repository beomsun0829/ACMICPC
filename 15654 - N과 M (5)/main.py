



ans = []

def dfs():
    if len(ans) == M:
        for k in range(len(ans)):
            print(ans[k] , end= ' ')
        print()
        return
    
    
    for i in range(N):
        now = arr[i]
        
        if now in ans:
            continue
        
        else:
            ans.append(arr[i])
            dfs()
            ans.pop()
    





def main():
    global N,M 
    N,M = map(int, input().split())
    
    global arr
    arr = list(map(int,input().split()))
    
    arr.sort()
    
    dfs()
    
    
main()