a,b=map(str,input().split())
di,di2={},{}
a1,b1,c=[],[],0
if len(a)!=len(b):
    print("no")
else:  
    for i in range(len(a)):
        if a[i] not in di:
            di[a[i]]=1
        else:      
            di[a[i]]=di[a[i]]+1
    for i in range(len(b)):
        if b[i] not in di2:
            di2[b[i]]=1
        else:
            di2[b[i]]=di2[b[i]]+1
    for keys in di:
        a1.append(di[keys])                                                         #using a hash concept
    for keys in di2:
        b1.append(di2[keys])
    for i in range(len(a1)):
        if a1[i]==b1[i]:
            c=c+1
    if len(a1)==c:
        print("yes")
    else:
        print("no")
