

def main():
    N, r, c = map(int,input().split())
    
    ans = 0
    while N != 0:
        size = pow(2, N)
        
        if r < size / 2 and c < size / 2:
            ans += 0
        
        elif r < size / 2 and c >= size / 2:
            ans += (size * size) / 4
            c -= size / 2
            
        
        elif r >= size / 2 and c < size / 2:
            ans += (size * size) / 4 * 2
            r -= size / 2
        
        elif r >= size / 2 and c >= size / 2:
            ans += (size * size) / 4 * 3
            r -= size / 2
            c -= size / 2
    
        N -= 1
    
    print(int(ans))
    
    
main()