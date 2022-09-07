import sys
sys.setrecursionlimit(10 ** 9)


class node():
    def __init__(self, node_number):
        self.parents = -1
        self.me = node_number
        
    def get_parents(self):
        return self.parents
    
    def set_parents(self, p):
        self.parents = p



def maketree(node):
    for i in range(len(con_list[node])):
        now = con_list[node][i]
        if data[now].get_parents() == -1:
            data[now].set_parents(node)
            maketree(now)
            
    return


def main():
    N = int(input())
    
    global data
    data = []
    data.append(node(0))
    
    for i in range(1, N + 1):
        data.append(node(i))
    
    global con_list
    con_list = []
    
    for i in range(N + 1):
        con_list.append([])
    
    for i in range(N - 1):
        a,b = map(int,sys.stdin.readline().split())
        con_list[a].append(b)
        con_list[b].append(a)
    
    maketree(1)
    
    for i in range(2, N + 1):
        print(data[i].get_parents())
    
    
main()