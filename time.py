a=int(input())
z=0
if a<60:
  print("0",a)
else:
  z=a//60
  a=a%60
  print(z,a)
