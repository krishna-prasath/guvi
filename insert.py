a,b=map(str,input().split())
a,b,temp=list(a),int(b),""
for i in range(b):
    temp=a[-1]
    a.remove(a[-1])
    a.insert(0,temp)
print("".join(a))
