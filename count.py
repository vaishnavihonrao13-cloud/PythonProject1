no=int(input("enter the number"))
count=0
while no>0:
    no=no//10
    count+=1
print("number of digit is:",count)