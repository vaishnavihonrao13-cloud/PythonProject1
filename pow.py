base=int(input("enter base:"))
index=int(input("enter index:"))
pow=1
while index>=1:
    pow=pow*base
    index-=1
print("power:",pow)
