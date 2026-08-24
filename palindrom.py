no=int(input("enter the number"))
rev=0
t=no
while no>0:
    rev=rev*10+no%10
    no=no//10
if rev==t:
    print("no is palindrom number")
else:
    print("no is not palindrom number")