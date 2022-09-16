

from math import inf


def main():
    N = int(input())
    A = list(map(int,input().split()))

    dp = [inf] * (N + 101)
    dp[0] = 1
    cnt = 0
    
    for i in range(len(A)):
        cnt += 1
        for j in range(1, A[i] + 1):
            dp[i + j] = min(dp[i + j], dp[i] + 1)
            
            if i + j == N - 1:
                break
    
    if(dp[N - 1] - 1 == inf):
        print(-1)
        return
        
    print(dp[N - 1] - 1)

        
    
    
main()