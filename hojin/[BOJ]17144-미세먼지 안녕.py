import sys
input= sys.stdin.readline


r,c,t=map(int,input().split())
air=[list(map(int,input().split())) for _ in range(r)]


#공기청정기 위치
top,bot=0,0
for i in range(c):
    if air[i][0]==-1:
        top=i
        bot=i+1
        break

def spreading():
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    air_temp=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if air[i][j]>0:
                
                dust=air[i][j]//5
                for k in range(4):
                    
                    nx=j+dx[k]
                    ny=i+dy[k]
                    
                    if 0<=nx<c and 0<=ny<r and air[ny][nx]>=0:

                        air_temp[ny][nx]+=dust
                        air_temp[i][j]-=dust                         

    for i in range(r):
        for j in range(c):
            air[i][j]+=air_temp[i][j]


def purify():
    
    temp=[[0]*c for _ in range(r)]
    ##위쪽
    #상단
    for i in range(1,c):
        temp[0][i-1]=air[0][i]
    #하단
    for i in range(1,c):
        temp[top][i]=air[top][i-1]

    #공기청정기 첫 바람
    temp[top][1]=0

    #좌단
    for i in range(1,top):
        temp[i][0]=air[i-1][0]
    temp[0][0]=air[0][1]
    #우단
    for i in range(top,-1,-1):
        temp[i-1][-1]=air[i][-1]
    temp[top][-1]=air[top][-2]



    ##아래쪽
    #상단
    for i in range(1,c):
        temp[bot][i]=air[bot][i-1]

    #공기청정기 첫 바람
    temp[bot][1]=0
    
    #하단
    for i in range(1,c):
        temp[-1][i-1]=air[-1][i]
    #좌단
    for i in range(bot+1,r):
        temp[i-1][0]=air[i][0]
    temp[-1][0]=air[-1][1]
    #우단
    for i in range(bot+1,r):
        temp[i][-1]=air[i-1][-1]
    temp[bot][-1]=air[bot][-2]
    
    #공기청정기
    temp[top][0]=-1
    temp[bot][0]=-1
    
    air[0]=temp[0]
    air[-1]=temp[-1]
    air[bot]=temp[bot]
    air[top]=temp[top]
    for i in range(r):
        air[i][0]=temp[i][0]
        air[i][-1]=temp[i][-1]


for _ in range(t):
    spreading()
    purify()
total=0
for i in range(r):
    for j in range(c):
        total+=air[i][j]
print(total+2)


