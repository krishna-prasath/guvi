n=int(input())
a=list(map(str,input().split()))
b=list(map(str,input().split()))
s,count=[],0
c="".join(a)
d="".join(b)
while (c!=d):
    temp=b[-1]
    b.remove(b[-1])
    b.insert(0,temp)
    count+=1
    d="".join(b)
print(count)
