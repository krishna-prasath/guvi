n,a=map(int,input().split())
li=list(map(int,input().split()))
c=False
for i in range(n):
    for j in range(i+1,n):
        if li[i]+li[j]==a:
            c=True
if c==False:
    print("no")
else:
    print("yes")
