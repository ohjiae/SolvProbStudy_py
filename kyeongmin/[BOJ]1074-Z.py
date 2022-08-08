import sys 
input = sys.stdin.readline 

N, r, c = map(int ,input().split())

def dfs(y, x, n) :
    global num 
    
    if n > 2 : 
        
        if y<=r<y+(n//2) and x<=c<x(n//2) :
            num += 2**(2*(n//2)-2) 
            dfs(y, x, n//2)

        elif y<=r<y+(n//2) and x+(n//2)<=c<x+(n//2)+(n//2) :
            num += 2**(2*(n//2)-2) *1

            dfs(y, x+(n//2), n//2)
        
        
        elif y+(n//2)<=r<y+(n//2)+(n//2) and x<=c<x+(n//2)    :
            num += 2**(2*(n//2)-2) *2

            dfs(y+(n//2), x , n//2)
            
        else :
            num += 2**(2*(n//2)-2) *3

            dfs(y+(n//2), x+(n//2), n//2)
    else : 
        for dy, dx  in [(0,0),(0,1),(1,0),(1,1)] :
            num +=1 
            if (y+dy) == r and (x+dx) == c : 
                print(num-1)


if N == 1 :
    print("0") 

else :                

    num = 0


    if 0<= r < 2**(N-1) and 0<= c < 2**(N-1) :
        num = 0
        dfs(0,0,2**(N-1))

    elif 0<=r<2**(N-1) and 2**(N-1)<=c<2**(N-2) :
        num = 2**(2*N-2) *1
        dfs(0,2**(N-1),2**(N-1))

    elif 2**(N-1)<=r<2**(N-2) and 0<=c<2**(N-1) :
        num = 2**(2*N-2) *2
        dfs(2**(N-1),0, 2**(N-1))

    else :
        num = 2**(2*N-2) *3
        dfs(2**(N-1), 2**(N-1), 2**(N-1))


    # print(tile)
    

