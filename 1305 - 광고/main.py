import sys
input = sys.stdin.readline





def getMinPossibleLength(sc):
    length = len(sc)
    pi = [0] * length
    j = 0
    
    for i in range(1, length):
        while j > 0 and sc[i] != sc[j]:
            j = pi[j-1]
        
        if sc[i] == sc[j]:
            j += 1
            pi[i] = j
    
    return N - pi[-1]
    
    


def main():
    global N
    N = int(input())
    sc = str(input().rstrip())
    
    
    print(getMinPossibleLength(sc))
    
main()