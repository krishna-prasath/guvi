a=int(input())
d=[]
if a==2:
    print(0)
else:
    for i in range(2,a):
        c=0
        for j in range(2,i+1):
            if i%j==0:
               c=c+1
        if c==1:
           d.append(i)
    print(*d)    
