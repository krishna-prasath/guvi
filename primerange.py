n,a=map(int,input().split())
z=[]
for i in range(n+1,a):
    c=0
    for j in range(2,i+1):
        if i%j==0:
            c=c+1
    if c==1:
        z.append(i)

print(*z)
