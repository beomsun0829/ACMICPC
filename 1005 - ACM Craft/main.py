
import sys



def main():
    T = int(input())
    
    while T:
        T -= 1
        
        linked_list = []
        indeg = []
        q = []
        result = []
        
        N, K = map(int,sys.stdin.readline().split())
        build_time = list(map(int,sys.stdin.readline().split()))
        
        for i in range(N):
            linked_list.append([])
            indeg.append(0)
            result.append(build_time[i])
             
        for _ in range(K):
            x,y = map(int,sys.stdin.readline().split())
            linked_list[x - 1].append(y - 1)
            indeg[y - 1] += 1
        
        W = int(input()) - 1
        
        
        for i in range(N):
            if indeg[i] == 0:
                q.append(i)
        
        
        while len(q) != 0:
            now_index = q.pop(0)
            if now_index == W:
                break
            
            for i in linked_list[now_index]:
                indeg[i] -= 1
                result[i] = max(result[i], result[now_index] + build_time[i])
                
                if indeg[i] == 0:
                    q.append(i)
                    
                
        print(result[W])
        
        
main()