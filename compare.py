a,b=map(str,input().split())
c=0
for i in range(len(a)):
    if a[i]!=b[i]:
        c=c+1
if c==1:
    print("yes")
else:
    print("no")
