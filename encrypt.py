a=input()
b=input()
x,y,res=[],[],[]
c=""
a1={chr(i+96):i for i in range(1,27)}
b1={i:chr(i+96) for i in range(1,27)}
for i in range(len(a)):
    x.append(a1[a[i]])
    y.append(a1[b[i]])
for i in range(len(x)):
    if x[i]+y[i]<26:
        res.append(x[i]+y[i])
    else:
        res.append((x[i]+y[i])-26)
for i in range(len(res)):
    c=c+b1[res[i]]
print(c)
