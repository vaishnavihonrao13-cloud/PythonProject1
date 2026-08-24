no=int(input("enter the number:"))
i=2
isPrime=True
while i<=no/2:
    if no%i==0:
        isPrime=False
        break
    i=i+1
if isPrime:
    print("prime")
else:
    print("not prime")