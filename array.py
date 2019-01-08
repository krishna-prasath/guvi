l=[]
s=0
a,b=map(int,input().split(" "))
for i in range(a):
    l.append(int(input()))
for i in range(b):
    s=s+l[i]
print(s)
