a=15
b=23
c=3
if a>b and a>c:
    print(a,"is greater than ",b"and ",c)
elif b>c:
    print(b,"is greater than ",c)
else:
    print(c,"is greater than ",b,c)

age=18
hasId = True
if age>=18:
    if hasId:
        print("permission granted")
    else:
        print("id needed")
else:
    print("permission denied")

no=0
if no>0:
    if no%2==0:
        print("no is +ve even number")
    else:
        print("no is +ve odd number")
else:
    if no==0:
        print("no is zero")
    else:
        print("no is negative")

