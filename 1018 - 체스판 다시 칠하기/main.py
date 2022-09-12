



from math import inf


def main():
    N,M = map(int,input().split())
    input_data = []
    for _ in range(N):
        input_data.append(input())
    
    data = []
    for i in range(N):
        data.append([])
        for j in range(M):
            if input_data[i][j] == 'W':
                data[i].append(0)
            else:
                data[i].append(1)
    
    
    ans_arr = []
    tmp = 0
    for i in range(8):
        ans_arr.append([])
        for j in range(8):
            if tmp == 0:
                ans_arr[i].append([0,1])
            else:
                ans_arr[i].append([1,0])
            tmp = (tmp + 1) % 2
        tmp = (tmp+1) % 2


    ans = inf
    
    for i in range(N - 8 + 1):
        for j in range(M - 8 + 1):
            
            for fl in range(2):
                cnt = 0
                for k in range(8):
                    for l in range(8):
                            if data[k + i][l + j] != ans_arr[k][l][fl]:
                                cnt += 1
                
                ans = min(ans, cnt)

    print(ans)
    
main()