


def main():
    L = int(input())
    S = list(map(int,input().split()))
    n = int(input())
    
    S.insert(0,0)
    S.append(1001)
    S.sort()
    
    index = -1
    
    for i in range(len(S)):
        if n < S[i]:
            index = i
            break
    
    
    start = S[index - 1]
    end = S[index]
    ans = 0
    
    for i in range(start + 1, end):
        for j in range(start + 1, end):
            if i < j and i <= n and j >= n:
                ans += 1

    print(ans)
    
    
main()