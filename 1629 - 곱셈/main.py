
def pow(num, e, C):
    if e == 1:
        return num % C
    
    half = pow(num, e//2, C)
    
    if e % 2 == 0:
        return half * half % C
    
    else:
        return half * half * num % C



def main():
    A,B,C = map(int,input().split())
     
    print(pow(A, B, C))



main()