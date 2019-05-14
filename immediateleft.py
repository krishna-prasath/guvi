n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n-1):
    if l[i]>l[i+1]:
        a.append(l[i+1])
    else:
        a.append(-1)
a.append(-1)
print(*a) #missed the * in the output
