a=input()
s=""
for i in range(1,len(a),2):
    s=s+a[i]+a[i-1]
print(s)
