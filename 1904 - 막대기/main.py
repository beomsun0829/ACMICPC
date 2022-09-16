
def main():
    X = int(input())
    
    stick = [64]
    
    while True:
        add = 0
        for i in range(len(stick)):
            add += stick[i]        
        if X == add:
            print(len(stick))
            break
        
        short = stick[len(stick) - 1]
        half = short / 2
        
        stick.pop()
        stick.append(half)
        
        add = 0
        for i in range(len(stick)):
            add += stick[i]
        
        if add < X:
            stick.append(half)
            add += half
    
    
main()