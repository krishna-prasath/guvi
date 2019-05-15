a=input()
di={}
a1,b1=[],[]
for i in range(len(a)):
    if a[i] not in di:
        di[a[i]]=1
    else:      
        di[a[i]]=di[a[i]]+1
for values in di:
    a1.append(di[values])
for v in di:
    b1.append(v)
x=a1[0]
for i in range(1,len(a1)):
    if x<a1[i]:
        x=a1[i]
        key=i
print(b1[key])
