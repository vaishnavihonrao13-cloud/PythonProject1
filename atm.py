amount = int(input("enter amount "))
n500, n200, n100 = 0, 0, 0
if amount >= 500:
    n500 = amount // 500
    amount %= 500
if n500 > 0:
    print("500:-", n500)
if amount >= 200:
    n200 = amount // 200
    amount %= 200
if n200 > 0:
    print("200:-", n200)
if amount >= 100:
    n100 = amount // 100
    amount %= 100
if n100 > 0:
    print("100:-", n100)