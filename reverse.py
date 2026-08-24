no=int(input("enter no:"))
rev=0
t=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
print("reverse of ",t,"is :",rev)