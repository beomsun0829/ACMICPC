

#인접행렬 말고 인접리스트 사용해야함, 우선순위큐

from math import inf


global dp, visited, data
data = []
dp = []
visited = []

def smallindex():
    min = inf
    index = 0
    for i in range(V):
        if dp[i] < min and visited[i] == False:
            min = dp[i]
            index = i
            
    return index


def dijkstra():
    for i in range(V):
        dp.append(data[K][i])
        visited.append(False)
        
    visited[K] = True
    
    for i in range(V-1):
        current = smallindex()
        visited[current] = True
        
        for j in range(V):
            if visited[j] == False:
                dp[j] = min(dp[current] + data[current][j], dp[j])



def main():
    global V,E,K
    V, E = map(int, input().split())
    K = int(input())
    K = K - 1
    
    for i in range(V):
        data.append([])
        for j in range(V):
            data[i].append(inf)
            if i == j:
                data[i][j] = 0
    
    
    for _ in range(E):
        u,v,w = map(int,input().split())
        data[u-1][v-1] = w
    
    dijkstra()
    
    for i in range(V):
        if dp[i]:
            print('INF')
        else:
            print(dp[i])

main()