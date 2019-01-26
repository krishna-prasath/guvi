a=int(input())
b=list(map(int,input().split()))
s=[]
for i in range(a):
    if b[i] in b[i+1:]:
        s.append(b[i])
b=set(b)
s=set(s)
b=b&s
if len(b)>0:
    print(*b)
else:
    print('unique')


        
