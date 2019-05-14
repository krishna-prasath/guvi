a=input()
b=input()
a1,b1,="","",
l1,l2=[],[]
for i in range(len(a)):
    if a[i]=='#':                                                     #may look complex but simple as hell
        a1=a[:i]
        break
for i in range(len(a)):
    if b[i]=='#':
       b1=b[:i]
       break
for i in range(len(a)-1):
    v=0
    if a[i]=='#':
        v=i+1
        if a[v:v+2].isnumeric():
            l1.append(int(a[v:v+2]))
        else:
            l1.append(int(a[v]))
for i in range(len(b)-1):
    v=0
    if b[i]=='#':
        v=i+1
        if b[v:v+2].isnumeric():
            l2.append(int(b[v:v+2]))
        else:
            l2.append(int(b[v]))  
        
if sum(l1)>sum(l2):
    print(a1)
else:
    print(b1)

