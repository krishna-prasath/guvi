a=input()
try:
    int(a,16)
    print("yes")
except ValueError:
    print("no")
