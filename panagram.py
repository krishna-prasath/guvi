a=input()
a=a.lower()
a=a.replace(" ","")
z=[]
for i in range(97,123):
    z.append(chr(i))
a,z=set(a),set(z)
c=z.difference(a)
if len(c)==0:
    print("yes")
else:
    print("no")
