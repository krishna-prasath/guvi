s=0
a,b=map(int,input().split(" "))
l=list(map(int,input().split(" ")))
for i in range(b):
    s=s+l[i]
print(s)
