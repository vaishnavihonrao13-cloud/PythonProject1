no=int(input("enter the number"))
t=no
sum=0
while no>0:
    rem=no%10
    sum=sum+rem*rem*rem
    no=no//10
if sum==t:
    print(no,"is armstrong number")
else:
    print(no,"is not armstrong number")