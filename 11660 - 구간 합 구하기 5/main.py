from sys import stdin


data = []
dp = []

def main():
    N,M = map(int,input().split())
    
    for _ in range(N):
        data.append(list(map(int, stdin.readline().split())))


    dp = [[0] * N for _ in range(N)]
    dp[0][0] = data[0][0]
    
    
    for j in range(1,N):
        dp[0][j] = dp[0][j-1] + data[0][j]
    
    
    for i in range(1,N):
        linesum = [data[i][0]]
        for j in range(1,N):
            linesum.append(linesum[j-1] + data[i][j])
        
        for j in range(N):
            dp[i][j] = dp[i-1][j] + linesum[j]
    
    for _ in range(M):
        x1, y1, x2, y2 = map(int,stdin.readline().split())
        x1 = x1 - 1
        y1 = y1 - 1
        x2 = x2 - 1
        y2 = y2 - 1
        
        ans = dp[x2][y2]
        if x1 > 0:
            ans -= dp[x1-1][y2]
        if y1 > 0:
            ans -= dp[x2][y1-1]
            
        if x1 > 0 and y1 > 0:
            ans += dp[x1-1][y1-1]
        
        print(ans)
        #1,1,4,4, 입력시 out of range
    
    
main()