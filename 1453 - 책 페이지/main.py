

numbers = []
def func(start, end, dex):
    global numbers
    
    while int(start % 10) != 0 and (start <= end):
        calc(start, dex)
        start += 1
    
    if start > end:
        return
    
    while (int(end % 10) != 9) and (start <= end):
        calc(end, dex)
        end -= 1
    
    cnt = (int(end / 10) - int(start / 10) + 1)
    
    for i in range(10):
        numbers[i] += cnt * dex
    
    func (start / 10 , end / 10, dex * 10)
        
        

def calc(num : int, inc):
    global numbers
    while num:
        numbers[int(num % 10)] += inc
        num = int(num / 10)
        
        

def main():
    global numbers
    for i in range(10):
        numbers.append(0)

    N = int(input())
    func(1, N, 1)
    
    for i in range(10):
        print(numbers[i] , end = " ")
        
    
main()