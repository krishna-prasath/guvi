a=int(input())
l=[]
for i in range(a):
    l.append(input())

s,d=[],[]
a1=['a','e','i','o','u']
for i in range(len(l)):
    c=0
    for j in range(len(l[i])):
        for k in range(len(a1)):
            if l[i][j].lower()==(a1[k]):
                c=c+1
    s.append(c)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]<s[j]:
            h=l[i]
            l[i]=l[j]
            l[j]=h
for i in range(a):
    print(l[i])

