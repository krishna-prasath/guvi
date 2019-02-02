a=int(input())
a1=[]
for i in range(1,a+1):
    c=0
    if a%i==0:
        x=i
        for j in range(2,x+1):
            if x%j==0:
                c=c+1
        if c==1:
            a1.append(i)
print(*a1)
        
