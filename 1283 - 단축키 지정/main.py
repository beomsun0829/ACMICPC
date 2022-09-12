



def setShortCut(string, dt):
    dt_cnt = 0
    for i in range(len(dt)):
        if not (dt[i][0].upper() in shortcut):
            shortcut.append(dt[i][0].upper())
            shortcut_index.append(dt_cnt)
            return
        
        dt_cnt += len(dt[i]) + 1

    for i in range(len(string)):
        if not (string[i].upper() in shortcut) and not(string[i] == ' '):
            shortcut.append(string[i].upper())
            shortcut_index.append(i)
            return

    shortcut.append('')
    shortcut_index.append(-1)



def main():
    N = int(input())
    
    global shortcut
    shortcut = []
    
    global shortcut_index
    shortcut_index = []
    
    saver = []
    
    for _ in range(N):
        string = input()
        dt = string.split(' ')
        
        saver.append(string)
        
        setShortCut(string,dt)
    
    for i in range(N):
        ans = ''
        
        for j in range(len(saver[i])):
            if shortcut_index[i] == j:
                ans += '[' + saver[i][j] + ']'
            else:
                ans += saver[i][j]
                
            
        print(ans)
        
        
    
        
main()