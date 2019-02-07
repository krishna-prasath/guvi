a=int(input())
for i in range(2**a):
    print(bin(i)[2:].zfill(a))
