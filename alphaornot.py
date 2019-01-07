n=input()
if len(n)==1:
    if ord(n) in range(97,123):  #ord() <-- u can use to get ascii values of the letter
        print("Alphabet")
    else:
        print("No")
else:
    print("No")
