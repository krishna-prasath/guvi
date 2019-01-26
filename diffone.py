a,b=map(str,input().split())
s=0
for i in range(len(a)):
    if a[i]!=b[i]:
        s=s+1
if s==1:
    print("yes")
else:
    print("no")
