n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
b=b[-1::-1]
c=0
for i in range(n):
    if a[i]==b[i]:
        c=c+1
if c==n:
    print("yes")
else:
    print("no")
