def main():
    n = int(input())
    
    A = []
    for i in range(n):
        tmp = (list(map(int,input().split())))
        A.append([tmp[0], tmp[1] * tmp[2] * tmp[3], tmp[1] + tmp[2] + tmp[3]])
        
    
    A.sort(key = lambda x:x[0])
    A.sort(key = lambda x:x[2])
    A.sort(key = lambda x:x[1])
    for i in range(3):
        print(A[i][0], end = ' ')
    
    

main()