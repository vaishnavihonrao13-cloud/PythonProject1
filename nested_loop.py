
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

