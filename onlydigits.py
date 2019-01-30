a=int(input())
b=list(map(int,input().split()))
s=[]
d=0
for i in range(a):
    if b[i] in b[i+1:]:
        s.append(b[i])
b=set(b)
s=set(s)
b=b.difference(s)
print(*b)
