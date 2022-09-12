from math import sqrt


def main():
    T = int(input())
    while T:
        T -= 1
        
        x, y = map(int, input().split())
        length = y - x
        d = int(sqrt(length))
        
        ans = 0
        
        if pow(d,2) == length:
            ans = 2 * d - 1
        else:
            ans = 2 * d
        if length > d*(d+1):
            ans += 1
        print(ans)
    
    
main()