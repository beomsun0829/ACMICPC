


def main():
    N = int(input())
    F = int(input())
    
    a = int(N / 100)
    a *= 100
    
    for i in range(100):
        if (a + i) % F == 0:
            if i < 10:
                print('0' + str(i))
                break
            print(i)
            break
    
    
    
    
main()