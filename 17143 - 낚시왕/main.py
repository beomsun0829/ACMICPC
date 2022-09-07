


global data
data = []

dirX = [0,-1,1,0,0]
dirY = [0,0,0,1,-1]

class Shark:
    def __init__(self,r,c,s,d,z):
        self.r = r
        self.c = c
        self.s = s
        self.d = d
        self.z = z
        
    def move(self):
        speed = self.s
        if self.d == 1 or self.d == 2:
            speed %= R
        elif self.d == 3 or self.d == 4:
            speed %= C
        
        
        while speed > 0:
            speed -= 1
            
            gorow = self.r + dirX[]
            
        



def main():
    global R,C,M
    R, C, M = map(int,input().split())
    
    sharklist = []
    
    for _ in range(M):
        r,c,s,d,z = map(int,input().split())
        sharklist.append(Shark(r,c,s,d,z))
    
    
    
    
    
main()