

import sys
import bisect




def main():
    global k
    m,n,k = map(int,input().split())
    
    dt = []
    
    for i in range(k):
        dt.append(list(map(int,sys.stdin.readline().split())))
    
    
    dt.sort(key=lambda x:x[1])
    dt.sort(key=lambda x:x[0])
    
    global S
    S = set()
    S.add(0)
    ans = 1
    
    for i in range(k):
        S_list = list(S)
        it = bisect.bisect_left(S_list,dt[i][1])
        it -= 1
        
        if it >= 0:
            S_list[it] = dt[i][1]
        
        else:
            ans += 1
            S_list.append(dt[i][1])
            
        S = set(S_list)

    
    print(ans)
    
    

main()