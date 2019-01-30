a,b=map(int,input().split())
c=[]
for i in range(a,b+1):
    e=0
    for j in range(2,i+1):
        if i%j==0:
            e=e+1
    if e==1:
        c.append(i)

print(len(c))
            
