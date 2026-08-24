no=int(input("enter the number"))
sq=no*no
t=no
isAutomorphic=True
while no>0:
    if no%10!=sq%10:
        isAutomorphic=False
        break
    no=no//10
    sq=sq//10
if isAutomorphic==True:
    print("Automorphic number")
else:
    print("Not Automorphic number")