
i=1
while i<=5:
    j=1
    while j<=5:
        print(" * ",end="")
        j+=1
    i+=1
    print( )

i=1
while i<=10:
    j=1
    while j<=10:
        print(i*j,end=" ")
        j+=1
    i+=1
    print( )

i=1
while i<=5:
    j=1
    while j<=i:
        print(" * ",end="")
        j+=1
    i+=1
    print()

i=1
while i<=5:
    j=i
    while j<=5:
        print(" * ",end="")
        j+=1
    i+=1
    print()

i = 1

while i <= 5:
    j = 1

    while j <= i:
        print(" * ", end="")
        j += 1

    i += 1
    print()
#mirror image
i = 1

while i <= 5:
    j = i

    while j < 5:
        print(" ", end="")
        j += 1

    j = 1

    while j <= i:
        print("* ", end="")
        j += 1

    i += 1
    print()
#mirror image
i = 1

while i <= 5:
    j = 1

    while j < i:
        print(" ", end="")
        j += 1

    j = i

    while j <= 5:
        print(" * ", end="")
        j += 1

    i += 1
    print()

i=1
n=10
while i<=n:
    j=1
    while j<=n:
        if i==1 or i==10 or j==1 or j==10:
            print(" * " ,end="")
        else:
            print("   ",end="")
        j+=1
    i+=1
    print()

#pyramid
i=1
n=10
while i<=n:
    j=i
    while j<n:
        print("  ",end="")
        j+=1
    j=1
    while j<=(i*2)-1:
        print("* ",end="")
        j+=1
    i+=1
    print()

