a,b,n=map(str,input().split())
n,c=int(n),0
for i in range(len(a)):
    if a[i]!=b[i]:
        c=c+1
if c==n:
    print("yes")
    
else:
    print("no")
