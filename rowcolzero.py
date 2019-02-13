a,b=map(int,input().split())
z=[]
for i in range(a):
    z.append(list(map(int,input().split())))
for i in range(a):
    for j in range(b):
        if z[i][j]==0:
            for k in range(a):
                z[k][j]='r'
            for m in range(b):
                z[i][m]='r'
for i in range(a):
    for j in range(b):
        if z[i][j]=='r':
            z[i][j]=0
for i in range(a):
    print(*z[i])
            
    
