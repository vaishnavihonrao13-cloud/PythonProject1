def add(a,b):
    res=a+b
    return res
result=add(10,20)
print("addition of is",result)

def reverse(no):
    rev=0
    while no>0:
        rem=no%10
        rev=rev*10+rem
        no=no//10
    return rev
no=int(input("enter a number"))
if no==reverse(no):
    print("number is palindrom")
else:
    print("number is not palindrom")
