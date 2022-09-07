


def factorial(a):
    if a == 1:
        return 1

    return factorial(a - 1) * a


def main():
    N,M = map(int,input().split())
    
    print(factorial(N) // factorial(N-M) // factorial(M))
    
main()