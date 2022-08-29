
map = []
dir = [[0,1],[0,-1],[1,0],[-1,0]]


def move(nowmap, direction):
    

def loop(nowmap, cnt):
    
    if cnt > 10:
        return -1
    
    for i in range(4):
        move(nowmap, dir[i])
    
    
    


def main():
    global map
    
    N,M = input().split()
    N , M = int(N), int(M)
    
    for _ in range(N):
        map.append(input()) 
    
    print(map)
    loop(0)
    
    
main()