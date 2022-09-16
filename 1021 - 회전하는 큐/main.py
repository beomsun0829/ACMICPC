




def main():
    N, M = map(int,input().split())
    
    q = list(map(int,input().split()))
    
    data = []
    for i in range(1, N + 1):
        data.append(i)
    
    ans = 0
    
    while len(q) != 0:
        now = q.pop(0)
        
        index = -1
        for i in range(len(data)):
            if data[i] == now:
                index = i
                break
        
            
        if index < len(data) - index:           #move left
            while now != data[0]:
                tmp = data.pop(0)
                data.append(tmp)
                ans += 1
        
        else:                           
            while now != data[0]:
                tmp = data.pop()
                data.insert(0,tmp)
                ans += 1
                
        data.pop(0)


    print(ans)
    
    
    
main()